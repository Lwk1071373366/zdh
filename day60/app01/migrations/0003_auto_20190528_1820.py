# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-28 10:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20190527_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publish',
            new_name='publishs',
        ),
    ]