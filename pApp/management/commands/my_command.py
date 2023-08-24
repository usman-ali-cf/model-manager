from django.core.management.base import BaseCommand, CommandError
# from practicing.pApp.models import Employee

from django.core.exceptions import ObjectDoesNotExist


class Command(BaseCommand):
    help = "Command will print name of app"

    def add_arguments(self, parser):
        parser.add_argument("times", nargs="+", type=int)
        parser.add_argument(
            "--detail",
            help="It will describe application in details",
        )

    def handle(self, *args, **options):
        if options['detail']:
            self.stdout.write("my Application: is a practicing app. Build in django ")
        else:
            for time in options['times']:
                try:
                    self.stdout.write("my Application")
                except ObjectDoesNotExist as e:
                    raise CommandError("Not Understandable :(")




