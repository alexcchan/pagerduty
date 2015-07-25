"""
API MAPPING FOR PagerDuty API V1
"""

mapping_table = {

    'content_type': 'application/json',
    'path_prefix': '/api/v1',

    'list_schedule_entries': {
        'method': 'GET',
        'path': '/schedules/{{schedule_id}}/entries',
        'valid_params': ['since', 'until', 'overflow', 'time_zone', 'user_id']
    },

}
