# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-06-05 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20190605_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publishDate',
            field=models.DateField(),
        ),
    ]
