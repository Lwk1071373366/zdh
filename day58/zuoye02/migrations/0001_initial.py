# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-24 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('price', models.FloatField()),
                ('date', models.DateField()),
                ('publisher', models.CharField(max_length=32)),
            ],
        ),
    ]
