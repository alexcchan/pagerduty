"""
API MAPPING FOR PagerDuty API V1
"""

mapping_table = {

    'content_type': 'application/json',
    'path_prefix': '/api/v1',

    # Alerts
    'list_alerts': {
        'method': 'GET',
        'path': '/alerts',
        'valid_params': ['offset', 'limit', 'since', 'until', 'filter[type]', 'time_zone']
    },

    # Escalation Policies
    'get_escalation_policy': {
        'method': 'GET',
        'path': '/escalation_policies/{{escalation_policy_id}}'
    },
    'list_escalation_policies': {
        'method': 'GET',
        'path': '/escalation_policies',
        'valid_params': ['offset', 'limit', 'query', 'teams', 'include']
    },
    'list_on_call_escalation_policies': {
        'method': 'GET',
        'path': '/escalation_policies/on_call',
        'valid_params': ['offset', 'limit', 'query']
    },
    'get_escalation_policy_rule': {
        'method': 'GET',
        'path': '/escalation_policies/{{escalation_policy_id}}/escalation_rules/{{escalation_rule_id}}'
    },
    'list_escalation_policy_rules': {
        'method': 'GET',
        'path': '/escalation_policies/{{escalation_policy_id}}/escalation_rules'
    },

    # Incidents
    'get_incident': {
        'method': 'GET',
        'path': '/incidents/{{incident_id}}'
    },
    'get_incidents_count': {
        'method': 'GET',
        'path': '/incidents/count',
        'valid_params': ['since', 'until', 'date_range', 'status', 'incident_key', 'service', 'teams', 'assigned_to_user']
    },
    'list_incidents': {
        'method': 'GET',
        'path': '/incidents',
        'valid_params': ['offset', 'limit', 'since', 'until', 'date_range', 'fields', 'status', 'incident_key', 'service', 'teams', 'assigned_to_user', 'time_zone', 'sort_by']
    },
    'list_incident_notes': {
        'method': 'GET',
        'path': '/incidents/{{incident_id}}/notes'
    },
    'create_incident': {
        'method': 'POST',
        'path': 'https://events.pagerduty.com/generic/2010-04-15/create_event.json'
    },

    # Log Entries
    'get_log_entry': {
        'method': 'GET',
        'path': '/log_entries/{{log_entry_id}}',
        'valid_params': ['time_zone', 'include']
    },
    'list_log_entries': {
        'method': 'GET',
        'path': '/log_entries',
        'valid_params': ['offset', 'limit', 'time_zone', 'since', 'until', 'is_overview', 'include']
    },
    'list_incident_log_entries': {
        'method': 'GET',
        'path': '/incidents/{{incident_id}}/log_entries',
        'valid_params': ['offset', 'limit', 'time_zone', 'since', 'until', 'is_overview', 'include']
    },
    'list_user_log_entries': {
        'method': 'GET',
        'path': '/users/{{user_id}}/log_entries',
        'valid_params': ['offset', 'limit', 'time_zone', 'since', 'until', 'is_overview', 'include']
    },

    # Maintenance Windows
    'get_maintenance_window': {
        'method': 'GET',
        'path': '/maintenance_windows/{{maintenance_window_id}}',
        'valid_params': ['include']
    },
    'list_maintenance_windows': {
        'method': 'GET',
        'path': '/maintenance_windows',
        'valid_params': ['offset', 'limit', 'query', 'service_ids', 'teams', 'filter', 'include']
    },

    # Schedules
    'get_schedule': {
        'method': 'GET',
        'path': '/schedules/{{schedule_id}}',
        'valid_params': ['since', 'until', 'time_zone']
    },
    'list_schedules': {
        'method': 'GET',
        'path': '/schedules',
        'valid_params': ['offset', 'limit', 'query', 'requester_id']
    },
    'list_schedule_entries': {
        'method': 'GET',
        'path': '/schedules/{{schedule_id}}/entries',
        'valid_params': ['since', 'until', 'overflow', 'time_zone', 'user_id']
    },
    'list_schedule_overrides': {
        'method': 'GET',
        'path': '/schedules/{{schedule_id}}/overrides',
        'valid_params': ['since', 'until', 'editable', 'overflow']
    },
    'list_schedule_users': {
        'method': 'GET',
        'path': '/schedules/{{schedule_id}}/users',
        'valid_params': ['since', 'until']
    },

    # Services
    'get_service': {
        'method': 'GET',
        'path': '/services/{{service_id}}',
        'valid_params': ['include']
    },
    'list_services': {
        'method': 'GET',
        'path': '/services',
        'valid_params': ['offset', 'limit', 'teams', 'include', 'include[]', 'time_zone', 'query', 'sort_by']
    },

    # Teams
    'get_team': {
        'method': 'GET',
        'path': '/teams/{{team_id}}'
    },
    'list_teams': {
        'method': 'GET',
        'path': '/teams',
        'valid_params': ['offset', 'limit', 'query']
    },

    # Users
    'get_user': {
        'method': 'GET',
        'path': '/users/{{user_id}}',
        'valid_params': ['include']
    },
    'get_user_on_call': {
        'method': 'GET',
        'path': '/users/{{user_id}}/on_call',
        'valid_params': ['include']
    },
    'list_users': {
        'method': 'GET',
        'path': '/users',
        'valid_params': ['offset', 'limit', 'query', 'include']
    },
    'list_on_call_users': {
        'method': 'GET',
        'path': '/users/on_call',
        'valid_params': ['offset', 'limit', 'query', 'include']
    },
    'get_user_contact_method': {
        'method': 'GET',
        'path': '/users/{{user_id}}/contact_methods/{{contact_method_id}}'
    },
    'list_user_contact_methods': {
        'method': 'GET',
        'path': '/users/{{user_id}}/contact_methods'
    },
    'get_user_notification_rule': {
        'method': 'GET',
        'path': '/users/{{user_id}}/notification_rules/{{notification_rule_id}}'
    },
    'list_user_notification_rules': {
        'method': 'GET',
        'path': '/users/{{user_id}}/notification_rules'
    },
}
