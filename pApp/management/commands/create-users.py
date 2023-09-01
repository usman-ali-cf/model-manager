from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from pApp.models import DateTime
from datetime import datetime
from pytz import timezone


class Command(BaseCommand):
    help = "Command will create users in database"

    def add_arguments(self, parser):
        parser.add_argument("number", type=int)

    def handle(self, *args, **options):
        for time in range(0, options['number']):
            try:
                id = len(User.objects.all()) + 1
                username = "username{id}".format(id=id)
                firstname = "fuser{id}".format(id=id)
                lastname = "luser{id}".format(id=id)
                password = "password{id}".format(id=id)
                user = User(username=username, password=password, last_name=lastname, first_name=firstname)
                user.save()
                date = datetime.now(timezone('Asia/Karachi'))
                pst_time = DateTime(time=date, format="PST")
                pst_time.save()
            except ObjectDoesNotExist as e:
                raise CommandError("Try running command as python manage.py create-user <int: numbers>")
        self.stdout.write(str(options['number']) + " Users has been created successfully created")
