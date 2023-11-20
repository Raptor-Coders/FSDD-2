from django.db import models

# Create your models here.

class EmailSubscription(models.Model):
    email = models.TextField(max_length=100, blank=True)
    isSubscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.email
    