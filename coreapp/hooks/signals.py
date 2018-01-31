from coreapp.models import Session
from django.dispatch import receiver
from django.db.models.signals import post_save
from coreapp.hooks import Hook
from django.forms.models import model_to_dict


@receiver(post_save)
def my_handler(sender, created, instance, **kwargs):
    if not sender.__module__ == 'coreapp.models':
        return
    hook_name = sender.__name__.lower()
    action_name = 'created' if created else 'updated'
    params = model_to_dict(instance)
    Hook.get_instance().call(hook_name, action_name, params)
