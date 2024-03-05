from django.db import models

# Create your models here.

class FormData(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255, default="")
    phone_number = models.CharField(max_length=20, default="")
    message = models.TextField()

    def __str__(self):
        return self.firstname