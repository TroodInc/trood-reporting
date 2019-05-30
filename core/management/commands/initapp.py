from django.core.management import BaseCommand


class Command(BaseCommand):
    """ Init backend command. """
    help = 'Init backend.'

    def handle(self, *args, **options):
        pass

