from django.core.management import BaseCommand
from code.importcoursedata import processcsv


class Command(BaseCommand):
    help = 'Import Course data from the csv file.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Trying to call processcsv')
        processcsv()
