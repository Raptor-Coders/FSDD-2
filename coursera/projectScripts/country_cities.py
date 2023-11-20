import argparse
import csv  # The csv module
from pprint import pprint

def main():
    """
    Entrypoint into the program
    """
    args = get_args() # retrieves filename from Command line
    countries_cities_ordered_list = get_csv(args.source) # returns dictionary using file source
    pprint (countries_cities_ordered_list)

def get_csv(filename):
    with open(filename, encoding='UTF-8', newline='') as file:
        csv_reader = csv.DictReader(file)
        list_of_dict = list(csv_reader)

        output_dict = {}

        for item in list_of_dict:
            country = item['Country']
            city = item['City']
            if country not in output_dict:
                output_dict[country] = []

            output_dict[country].append(city)

        return output_dict # returns dictionary of country / list of list of cities

        # pprint(output_dict)
 
def get_args(args=None):
    """
    Parse and return command line argument values
    """
    parser = argparse.ArgumentParser(description='Countries and Cities list.')
    parser.add_argument('--source', help='filename')
    return parser.parse_args(args)