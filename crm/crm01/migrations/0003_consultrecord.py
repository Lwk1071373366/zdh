# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-06-13 00:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm01', '0002_auto_20190611_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(verbose_name='跟进内容...')),
                ('status', models.CharField(choices=[('A', '近期无报名计划'), ('B', '1个月内报名'), ('C', '2周内报名'), ('D', '1周内报名'), ('E', '定金'), ('F', '到班'), ('G', '全款'), ('H', '无效')], help_text='选择客户此时的状态', max_length=8, verbose_name='跟进状态')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='跟进日期')),
                ('delete_status', models.BooleanField(default=False, verbose_name='删除状态')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to=settings.AUTH_USER_MODEL, verbose_name='跟进人')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm01.Customer', verbose_name='所咨询客户')),
            ],
        ),
    ]
