from celery import shared_task
from raptor_mailosaur.mailer import new_student_mailer
from raptor_mailosaur.mailer import new_subscription_mailer
# from students.models import Student
from email_subscriptions.models import EmailSubscription
from raptor_logger.raptor_logger import logger

'''
The @shared_task decorator in Celery is a convenient way to define tasks in
a Django application without needing to create a separate Celery application
instance. It allows us to use Celery tasks within a Django project more
seamlessly.
How @shared_task works:
Integration with Django: @shared_task is part of celery but designed to work
well with Django. It's particularly useful for Django projects that want to
incorporate Celery for handling asynchronous tasks.
Decorator Usage: We can decorate a regular Python function with @shared_task
to turn it into a Celery task. This means that the function can be executed
asynchronously by Celery workers.
'''
# @shared_task
# def send_email_to_student(param):
#     print('I am in the task')
#     send_email()

@shared_task
def create_subscription_for_new_student(email):
    logger.info('Subcription created for new student')
    es = EmailSubscription(
        email=email, 
        isSubscribed=True)
    es.save()
    print('new Email subscription created')

@shared_task
def send_welcome_email_to_student(param):
    print('Welcome email to student')
    # send_email()
    new_student_mailer()
    print(param)

@shared_task
def send_subscription_email_to_student(param):
    print('Subscription email to student')

    print(param)
    # send_email()
    new_subscription_mailer()