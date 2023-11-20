from django.db import models

# Create your models here.
class EmailSubscription(models.Model):
    email = models.EmailField(max_length=100)
    isSubscribed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.email


    # @staticmethod
    # def create_instance(message):
    #     return EmailSubscription.objects.create(email = message, isSubscribed=True)
        

