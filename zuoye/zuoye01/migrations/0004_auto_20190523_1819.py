# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-23 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zuoye01', '0003_auto_20190523_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='look_book',
            fields=[
                ('序号', models.AutoField(primary_key=True, serialize=False)),
                ('书籍名称', models.CharField(max_length=32)),
                ('书籍价格', models.FloatField()),
                ('出版时间', models.DateField()),
                ('出版社', models.CharField(max_length=32)),
            ],
        ),
        migrations.DeleteModel(
            name='look_books',
        ),
    ]
