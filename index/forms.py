from secrets import choice
from django.db import models
from socket import fromshare
from django import forms
from .models import *


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'subject', 'email','phone','body']