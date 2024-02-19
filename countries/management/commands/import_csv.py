from typing import Any
from django.core.management.base import BaseCommand, CommandParser
import csv  # The csv module
from pprint import pprint

class Command(BaseCommand):
    help = 'Displays countries and cities from csv file'

    def add_arguments(self, parser):
        """
        Parse and return command line argument values
        """
        parser.add_argument('filename', type=str, help='filename')
    
    def handle(self, *args: Any, **kwargs: Any) -> str | None:
        filename = kwargs['filename']
        newline = '\n'
        with open(filename, newline='') as file:
            csv_reader = csv.DictReader(file)
            list_of_dict = list(csv_reader)

            output_dict = {}

            for item in list_of_dict:
                country = item['Country']
                city = item['City']
                if country not in output_dict:
                    output_dict[country] = []

                output_dict[country].append(city)

            print(f'{newline} Requested CSV data: {newline}')
            pprint(output_dict)
            print(f'{newline} CSV filepath confirmation:{newline} \"{filename}\"{newline}')


