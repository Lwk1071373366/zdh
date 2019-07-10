from django.db import models

# Create your models here.

class book(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()
    date = models.DateField()
    publisher = models.CharField(max_length=32)
    modify_time = models.DateTimeField(auto_now=True)
