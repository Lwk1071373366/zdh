from django.db import models

# Create your models here.


class Book(models.Model):
    #配置属性 , ID 不写默认创建
    name = models.CharField(max_length=32)
    price = models.FloatField()
    date = models.DateField()
    publisher = models.CharField(max_length=32)
    modify_time = models.DateTimeField(auto_now=True)


class User(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    # def __str__(self):
    #     return self.username,self.password
