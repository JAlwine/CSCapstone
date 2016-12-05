# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 01:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ProjectsApp', '0003_merge_20161127_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='createdBy',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='experience',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='languages',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='speciality',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
