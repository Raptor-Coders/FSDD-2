import os.path
from typing import Any
from django.core.management.base import BaseCommand
import csv
from pprint import pprint
from students.models import Student
from courses.models import Course

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, '../../data/students.csv')

class Command(BaseCommand):
    help = 'Import data from fixture file data/students.csv'

    def handle(self, *args: Any, **options: Any) -> str | None:
        try:
            if Student.objects.exists():
                Student.objects.all().delete()

            with open(path, newline='') as file:
                csv_reader = csv.DictReader(file)
                list_of_students = list(csv_reader)

                for student in list_of_students:
                    course = Course.objects.get(name = student['course'])
                    
                    student = Student(course = course,
                                    fullname = student['fullname'],
                                    email = student['email'],
                                    phone = student['phone'])
                
                    student.save()

            print(Student.objects.all())
        
        except Exception as e:
            print(e)
