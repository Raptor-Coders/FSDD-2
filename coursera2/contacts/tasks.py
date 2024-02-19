from celery import shared_task
from raptor_mailosaur.mailer import new_contact_mailer

@shared_task
def send_email_to_new_contact(param):
    new_contact_mailer()