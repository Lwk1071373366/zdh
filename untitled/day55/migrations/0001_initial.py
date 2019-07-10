# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-22 09:58
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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('price', models.FloatField(null=True)),
            ],
        ),
    ]
