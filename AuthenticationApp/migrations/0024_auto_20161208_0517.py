# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0023_auto_20161207_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='projects',
        ),
        migrations.RemoveField(
            model_name='bookmark',
            name='user',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='project',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='userID',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
