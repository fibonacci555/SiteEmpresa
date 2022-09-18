from django.db import models
from phone_field import PhoneField

# Create your models here


class Contact(models.Model):
    name = models.CharField(null=False, default="", blank=False, max_length=200)
    subject = models.CharField(null=False, default="", blank=False, max_length=300)
    email = models.EmailField(null=False, default="", blank=False)
    phone = models.CharField(null=False, default="", blank=False, max_length=20)
    body = models.TextField(null=True,blank=True, max_length=1200)

    def __str__(self):
        return self.name