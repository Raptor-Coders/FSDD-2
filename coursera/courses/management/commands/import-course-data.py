from typing import Any
from django.core.management.base import BaseCommand, CommandParser
import csv
from pprint import pprint
from courses.models import Course
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, '../../data/courses.csv')



class Command(BaseCommand):
    help = 'Import data from fixture file data/courses.csv'

    def handle(self, *args: Any, **kwargs: Any) -> str | None:
        newline = '\n'

        if Course.objects.exists():
           existing_courses = Course.objects.all()
           existing_courses.delete()


        with open(path, newline='') as file:
            csv_reader = csv.DictReader(file)
            list_of_dict = list(csv_reader)

            output_dict = {} # dict to hold csv data

            # Loop to iterate through csv reader items & Course model
            for item in list_of_dict: 

                # assigning variables to csv reader items
                name = item['name']
                description = item['description']
                sessions = item['sessions']
                session_duration = item['session_duration']
                start_date = item['start_date']
                end_date = item['end_date']
                tags = item['tags']
                is_featured = item['is_featured']
                is_active = item['is_active']
                is_hidden = item['is_hidden']
                image_url = item['image_url']
                max_students = item['max_students']

                # collecting csv reader items in the python dict
                output_dict[name] = [description, sessions, session_duration, start_date, end_date, \
                                     tags, is_featured, is_active, is_hidden, image_url, max_students]

                # creating an instance of Course model
                new_course = Course()

                # assigning variables to Course model attributes
                new_course.name = name
                new_course.description = description
                new_course.sessions = sessions
                new_course.session_duration = session_duration
                new_course.start_date = start_date
                new_course.end_date = end_date
                new_course.tags = tags
                new_course.is_featured = is_featured
                new_course.is_active = is_active
                new_course.is_hidden = is_hidden
                new_course.image_url = image_url
                new_course.max_students = max_students

                # save to database
                new_course.save()

        print(Course.objects.all())
