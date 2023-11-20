from django.core.management import BaseCommand
from code.importstudentdata import processcsv

class Command(BaseCommand):
    help = 'Import Student data from the csv file.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        processcsv()
