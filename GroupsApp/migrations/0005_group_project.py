# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0006_auto_20161205_1702'),
        ('GroupsApp', '0004_group_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='project',
            field=models.ManyToManyField(to='ProjectsApp.Project'),
        ),
    ]
