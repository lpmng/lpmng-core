from django.test import TestCase
from unittest.mock import MagicMock, patch, sentinel
import os
import tests
import coreapp.hooks


class HookTestCase(TestCase):
    test_config = {
        'user': {
            'post_create': {
                    'url': ['https://callback/url']
                }
            }
        }

    def test_get(self):
        with patch('coreapp.hooks.Hook.__init__', return_value=None):
            instance1 = coreapp.hooks.Hook.get_instance()
            instance2 = coreapp.hooks.Hook.get_instance()

            self.assertIs(instance1, instance2)
            self.assertIsInstance(instance1, coreapp.hooks.Hook)

    def test_load_config(self):
        fake_instance = MagicMock()
        coreapp.hooks.Hook.load_config(
            fake_instance,
            os.path.join(tests.settings.BASE_DIR,
                         'tests/fixtures/test_hook_config.yml'))
        self.assertDictEqual(fake_instance.config, self.test_config)

    def test_call(self):
        fake_instance = MagicMock()
        fake_instance.config = self.test_config
        test_action = {'url': MagicMock()}

        fake_instance.actions = test_action

        coreapp.hooks.Hook.call(
            fake_instance, 'user', 'post_create', sentinel.param)
        test_action['url'].assert_called()

    def test_register_action(self):
        coreapp.hooks.Hook.register_action('test_action', sentinel.test_action)
        self.assertIn('test_action', coreapp.hooks.Hook.actions)
        self.assertEqual(coreapp.hooks.Hook.actions.get('test_action'),
                         sentinel.test_action)
