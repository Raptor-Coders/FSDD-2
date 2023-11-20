import csv
import os
#import sys
#sys.path.append('..')
from courses.models import Course

#
# Version 1.0.0
#
# This script takes a CSV file as input 

def main():
    processcsv()


def processcsv():
    filenm = 'data\courses.csv'
    cntrydict = {}

    if os.path.isfile(filenm):
        try:
            print('We going to try to import')
            # delete all records in table before importing data
            Course.objects.all().delete()

            with open(filenm,'r', newline='') as csvfile:
                csvrdr = csv.DictReader(csvfile, delimiter=',')

                for row in csvrdr:
                    crse = Course(name = row['name'], 
                                  description = row['description'],
                                  sessions = row['sessions'],
                                  session_duration = row['session_duration'],
                                  start_date = row['start_date'],
                                  end_date = row['end_date'],
                                  tags = row['tags'],
                                  is_featured = row['is_featured'],
                                  is_active = row['is_active'],
                                  is_hidden = row['is_hidden'],
                                  image_url = row['image_url'],
                                  max_students = row['max_students'])
                    crse.save()
                    print(crse)
        
        except IOError:
            print(f"An error occured trying to read from file: {filenm}")

        except Exception as e:
            print(f"Sorry, something went wrong trying to process the CSV file: {filenm}")
            print(e)

    else:
        print(f"Sorry, an error occured. Could not find file: {filenm}")


if __name__ == "__main__":
    main()


