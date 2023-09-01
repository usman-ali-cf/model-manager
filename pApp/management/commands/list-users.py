from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Command will list users from database"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            users = User.objects.all()
            self.stdout.write("Username" + ' - ' + "Password")
            self.stdout.write("------------------------------")
            for user in users:
                self.stdout.write(user.username + ' - ' + user.password)
            self.stdout.write("------------------------------")
        except ObjectDoesNotExist as e:
            raise CommandError("Try running command as python manage.py list-user")
