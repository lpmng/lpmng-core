import yaml
import os
import pathlib
import requests


class Hook:
    instance = None
    actions = {}

    def __init__(self):
        dir_path = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))
        hook_file_path = dir_path.joinpath('config.yml')

        self.config = None
        self.load_config(hook_file_path)

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()

        return cls.instance

    def call(self, hook_name, action_name, param):
        hook_object = self.config.get(hook_name)
        if not hook_object:
            return
        hook_actions = hook_object.get(action_name)
        if not hook_actions:
            return

        for action_type, action in self.actions.items():
            for hook_action in hook_actions.get(action_type, []):
                action(hook_action, hook_name, action_name, param)

    @classmethod
    def register_action(cls, action_name, action_class):
        cls.actions[action_name] = action_class

    def load_config(self, hook_file_path):
        with open(hook_file_path) as config_file:
            self.config = yaml.safe_load(config_file)


def hook_action_url(action_param, hook_name, hook_action, param):
    requests.post(
        action_param,
        json={'name': hook_name,
              'action': hook_action,
              'param': param})


Hook.register_action('url', hook_action_url)
