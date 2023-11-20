from django.db import models

# Create your models here.

class Contact(models.Model):
    fullname = models.TextField(max_length=200, blank=False)
    email = models.TextField(max_length=100, blank=True)
    phone = models.TextField(max_length=20)
    query = models.TextField(max_length=500)

    def __str__(self): 
        return self.fullname
    
