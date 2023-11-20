import csv
import os
from students.models import Student
from courses.models import Course

#
# Version 1.0.0
#
# This script takes a CSV file as input 

def main():
    processcsv()


def processcsv():
    filenm = 'data\students.csv'
    cntrydict = {}

    if os.path.isfile(filenm):
        try:
            print('We going to try to import')
            # delete all records in table before importing data
            Student.objects.all().delete()
            
            with open(filenm,'r', newline='') as csvfile:
                csvrdr = csv.DictReader(csvfile, delimiter=',')

                # we only have one course (id=5) register everyone to the one course
                #crseobj = Course.objects.get(id=5)
                try:
                    for row in csvrdr:
                        crsname = row['course']
                        crseobj = Course.objects.get(name=crsname)

                        stdnt = Student(course_id = crseobj, 
                                        fullname = row['fullname'],
                                        email = row['email'],
                                        phone = row['phone'])
                        stdnt.save()
                        print(stdnt)

                except Course.DoesNotExist:
                    print(f'Course: [{crsname}], does not exist in the Courses table.')
                except Course.MultipleObjectsReturned:
                    print(f'Course: [{crsname}], multiple records exist with this name.')
        
        except IOError:
            print(f"An error occured trying to read from file: {filenm}")

        except Exception as e:
            print(f"Sorry, something went wrong trying to process the CSV file: {filenm}")
            print(e)

    else:
        print(f"Sorry, an error occured. Could not find file: {filenm}")


if __name__ == "__main__":
    main()
