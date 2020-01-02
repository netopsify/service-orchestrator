# Ansible Filters

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from jinja2 import TemplateError
import json
import yaml

class FilterModule(object):

    def filters(self):
        return {
            'json_string_to_object': self.json_string_to_object,
            'json_object_to_yaml': self.json_object_to_yaml,
            'jira_story_subtasks_results': self.jira_story_subtasks_results,
            'single_jira_issue_extract': self.single_jira_issue_extract,
            }

    def json_string_to_object(self, s, *argv):
        return json.loads(s)

    def json_object_to_yaml(self, s, *argv):
        return yaml.dump(s)

    def jira_story_subtasks_results(self, s, *argv):
        jira_story = dict()
        _ = jira_story.update({"jira_story_subtasks_data": []})
        for jira_task in s:
            content = jira_task['json']
            task_description_list = content['fields']['description'].split('\r\n')
            task_description_replace = [
                t.replace(' - ', ',').replace('\u00a0', ',').replace(' on port ', ',') for t in task_description_list
                ]
            task_description = [x for x in task_description_replace if x != ""]
            _ = jira_story['jira_story_subtasks_data'].append(
                {
                    'task_description': task_description,
                    'project_id': content['fields']['project']['id'],
                    'project_name': content['fields']['project']['name'],
                    'project_key': content['fields']['project']['key'],
                    'task_status': content['fields']['status']['name'],
                    'task_priority': content['fields']['priority']['name'],
                    'task_summary': content['fields']['summary'],
                    'task_key': content['key'],
                    'task_id': content['id'],
                    'task_self': content['self']
                }
            )

        return json.dumps(jira_story)

    def single_jira_issue_extract(self, s, *argv):
        jira_story = dict()
        _ = jira_story.update({"jira_story_subtasks_data": []})
        jira_task = s
        content = jira_task['json']
        task_description_list = content['fields']['description'].split('\r\n')
        task_description_replace = [
            t.replace(' ', ',').replace('\u00a0', ',') for t in task_description_list
            ]
        task_description = [x for x in task_description_replace if x != ""]
        _ = jira_story['jira_story_subtasks_data'].append(
            {
                'task_description': task_description,
                'project_id': content['fields']['project']['id'],
                'project_name': content['fields']['project']['name'],
                'project_key': content['fields']['project']['key'],
                'task_status': content['fields']['status']['name'],
                'task_priority': content['fields']['priority']['name'],
                'task_summary': content['fields']['summary'],
                'task_key': content['key'],
                'task_id': content['id'],
                'task_self': content['self']
            }
        )

        return json.dumps(jira_story)