# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-29 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zuoye02', '0002_book_modify_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
    ]
