from django.db import models
from .tasks import send_email_to_new_contact

from django.db.models.signals import post_save
from django.dispatch import receiver

class Contact(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    query = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.fullname
    

@receiver(post_save, sender=Contact) # listen to django model events
def create_contact(sender, instance, created, **kwargs):
    if created:
        send_email_to_new_contact.delay('New email sent to new contact') # producer in terms of RabbitMQ
