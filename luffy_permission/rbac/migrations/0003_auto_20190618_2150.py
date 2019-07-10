# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-06-18 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0002_auto_20181030_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=32, null=True, verbose_name='一级菜单')),
                ('icon', models.CharField(blank=True, max_length=32, null=True, verbose_name='图标')),
            ],
        ),
        migrations.RemoveField(
            model_name='permission',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='is_menu',
        ),
        migrations.AddField(
            model_name='permission',
            name='pid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.Permission'),
        ),
        migrations.AddField(
            model_name='permission',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.Menu'),
        ),
    ]
