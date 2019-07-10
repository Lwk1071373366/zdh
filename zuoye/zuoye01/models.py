from django.db import models


# Create your models here.


#建表

# class look_books(models.Model):
#     id = models.AutoField(primary_key=True)
#     bname = models.CharField(max_length=32)
#     bprice = models.FloatField()
#     publication_date = models.DateField()
#     publishing_house = models.CharField(max_length=32)


class look_book(models.Model):
    序号 = models.AutoField(primary_key=True)
    书籍名称 = models.CharField(max_length=32)
    书籍价格 = models.FloatField()
    出版时间 = models.DateField()
    出版社 = models.CharField(max_length=32)
