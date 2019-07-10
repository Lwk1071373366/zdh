from django.db import models
# Create your models here.

class Author(models.Model):#作者表
    name=models.CharField( max_length=32)
    age=models.IntegerField()
    ad = models.OneToOneField(to='AuthorDetail')#默认找主键。默认级联


class AuthorDetail(models.Model):#作者详细信息表
    birthday=models.DateField()
    telephone=models.BigIntegerField()
    addr=models.CharField( max_length=64)

class Publish(models.Model):#出版社表
    name=models.CharField( max_length=32)
    city=models.CharField( max_length=32)

class Book(models.Model): #书籍表
    title = models.CharField( max_length=32)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    publishs=models.ForeignKey(to="Publish")
    authors=models.ManyToManyField(to='Author',)#生成第三张表
    def __str__(self):
        return self.title