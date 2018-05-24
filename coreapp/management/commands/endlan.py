from django.core.management.base import BaseCommand, CommandError
from coreapp.models import User, Session

class Command(BaseCommand):
    help = "Reset sessions after a lan"

    def handle(self, *args, **options):
        for user in User.objects.all():
            user.nbSessions = 0
            user.save()

        Session.objects.all().delete() 
        self.stdout.write(self.style.SUCCESS('Deleted all sessions and reseted nbSessions to 0 for everyone'))

