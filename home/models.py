from ast import Return
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import DateField

# Create your models here.
class Contact(models.Model):
    name  = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    description = models.TextField()
    date  = models.DateField()

def __str__(self):
        return self.name

