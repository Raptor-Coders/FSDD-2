import os
from celery import Celery

# celery -A raptorcoders_courses worker -l info --pool=solo
# need to add --pool to get it to run properly under windows

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'raptorcoders_courses.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'raptor_coursera.settings')
app = Celery('raptorcoders_courses')

# app.conf.beat_schedure = 'django_celery_beat.schedures:DatabaseScheduler'
app.config_from_object('django.conf.settings', namespace='CELERY')
app.autodiscover_tasks()