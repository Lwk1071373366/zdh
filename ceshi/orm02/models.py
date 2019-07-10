from django.db import models

# Create your models here.


class Books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    price = models.FloatField(null=True)