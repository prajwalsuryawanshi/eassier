from django.db import models

# Create your models here.
from django import forms


class geteassy(forms.Form):
    eassy = forms.CharField(max_length=2500)
