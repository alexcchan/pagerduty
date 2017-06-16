"""
   Wrapper for the PagerDuty API.  Based on the Python Zendesk library by Max
   Gutman <max@eventbrite.com>.
"""


import httplib2
import re
import urllib
try:
    import simplejson as json
except:
    import json

from datetime import datetime
from endpoints_v1 import mapping_table as mapping_table_v1
from httplib import responses


PAGER_DUTY_BASE_URL = 'https://%s.pagerduty.com'
DEFAULT_HTTP_METHOD = 'GET'
DEFAULT_HTTP_STATUS_CODE = 200
DEFAULT_CONTENT_TYPE = 'application/json'


class PagerDutyError(Exception):
    def __init__(self, msg, error_code=None):
        self.msg = msg
        self.error_code = error_code

    def __str__(self):
        return repr('%s: %s' % (self.error_code, self.msg))


def kwargs_to_params(kwargs):
    params = []
    for key, value in kwargs.iteritems():
        if hasattr(value, '__iter__'):
            if key.endswith('[]'):
                for v in value:
                    params.append((key,v))
            else:
                params.append((key,','.join(map(str, value))))
        else:
            params.append((key,value))
    return params


class PagerDuty(object):

    def __init__(self, subdomain=None, token=None, api_version=1, client_args={}):
        self.subdomain = subdomain
        self.token = token
        if api_version == 1:
            self.mapping_table = mapping_table_v1
        else:
            raise ValueError("Unsupported PagerDuty API Version: %d" %
                    api_version)
        self.client = httplib2.Http(**client_args)

    def __getattr__(self, api_call):
        def call(self, **kwargs):
            api_map = self.mapping_table[api_call]
            method = api_map.get('method', DEFAULT_HTTP_METHOD)
            status = api_map.get('status', DEFAULT_HTTP_STATUS_CODE)
            valid_params = api_map.get('valid_params', [])
            body = kwargs.pop('data', None)
            api_map_path = api_map.get('path','')
            if api_map_path.startswith('https://'):
                url_template = api_map_path
            else:
                path = self.mapping_table.get('path_prefix','') + api_map_path
                url_template = PAGER_DUTY_BASE_URL % self.subdomain + path
            url = re.sub(
                    '\{\{(?P<m>[a-zA-Z_]+)\}\}',
                    lambda m: "%s" % urllib.quote(str(kwargs.pop(m.group(1),''))),
                    url_template
            )
            for kw in kwargs:
                if kw not in valid_params:
                    raise TypeError("%s() got an unexpected keyword argument "
                            "'%s'" % (api_call, kw))
            url += '?' + urllib.urlencode(kwargs_to_params(kwargs))
            return self._make_request(method, url, body, status)
        return call.__get__(self)

    def _make_request(self, method, url, body, status):
        headers = {}
        if self.token:
            headers["Authorization"] = "Token token=%s" % self.token
        if body:
            content_type = self.mapping_table.get('content_type', DEFAULT_CONTENT_TYPE)
            headers["Content-Type"] = content_type
            if isinstance(body, dict):
                if content_type == 'application/x-www-form-urlencoded':
                    body = urllib.urlencode(body)
                elif content_type == 'application/json':
                    body = json.dumps(body)
        response,content = self.client.request(url, method=method, body=body,
                headers=headers)
        return self._response_handler(response, content, status)

    def _response_handler(self, response, content, status):
        if not response:
            raise PagerDutyError('Response Not Found')
        response_status = int(response.get('status', 0))
        if response_status != status:
            raise PagerDutyError(content, response_status)
        if response.get('location'):
            return response.get('location')
        elif content.strip():
            return json.loads(content)
        else:
            return responses[response_status]

    @staticmethod
    def date_string(d=None):
        """Format date/time according to PagerDuty ISO 8601."""
        if d is None:
            d = datetime.utcnow()
        return d.strftime('%Y-%m-%dT%H:%M:%SZ')
