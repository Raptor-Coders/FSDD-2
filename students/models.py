from django.db import models
from courses.models import Course
from email_subscriptions.models import EmailSubscription
from .tasks import some_task

from django.db.models.signals import post_save
from django.dispatch import receiver

import logging

# Configure the logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('student model')

# Create your models here.

class Student(models.Model):
    course_id = models.ForeignKey(Course, null=True, on_delete=models.RESTRICT)
    fullname = models.TextField(max_length=200, blank=True)
    email = models.TextField(max_length=100, blank=True)
    phone = models.TextField(max_length=20)

    def __str__(self):        
        return self.fullname
    

#@receiver(post_save, sender=Student) 
#def create_student(sender, instance, created, **kwargs):
#    if created:
#        print(instance)
#        print(' Created:')

"""
@receiver(post_save, sender=Student)
def save_emailsubscription(sender, instance, created, **kwargs):
    logger.debug('post_save got called by Student class')
    if created:
        logger.info('Student object got created successfully!')
        submail = EmailSubscription()
        submail.email = instance.email
        submail.save()
        print(f' Created an email subscription for: {submail.email}')
"""

@receiver(post_save, sender=Student)
def send_email(sender, instance, created, **kwargs):
        logger.debug('post_save got called by Student class')
        if created:
            print(instance)
            logger.info('Student object got created successfully!')
            some_task.delay('Student object has been created ')            
