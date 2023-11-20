from django.db import models
from courses.models import Course
# from emailSender import sender
from email_subscriptions.models import EmailSubscription

from django.db.models.signals import post_save
from django.dispatch import receiver

from raptor_logger.raptor_logger import logger
from .tasks import send_subscription_email_to_student
from .tasks import send_welcome_email_to_student
from .tasks import create_subscription_for_new_student

import logging

# Configure the logger
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger('my_logger')

class Student(models.Model):
    course = models.ForeignKey(Course,related_name='course', on_delete=models.RESTRICT,)
    fullname = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.fullname
    
# def create_subscription():
# def create_student():
#     new_student = Student()
#     if new_student:
#         create_subscription_for_new_student.delay('New Subscription has been created')

@receiver(post_save, sender=Student)
def create_subscription(sender, instance, created, **kwargs):
    logger.debug('post_save got called by Student class')
    if created:
        create_subscription_for_new_student.delay(instance.email)
        # es =  EmailSubscription()
        # es.email = instance.email
        # es.isSubscribed = True
        # es.save()
        logger.info('Student object got created successfully')
        send_subscription_email_to_student.delay('Student has been created ' + instance.fullname)
        send_welcome_email_to_student.delay('Student' + instance.fullname + 'with email' + instance.email +'has been created ' )

    

