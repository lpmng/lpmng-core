from django.apps import AppConfig


class CoreappConfig(AppConfig):
    name = 'coreapp'

    def ready(self):
        import coreapp.hooks.signals
