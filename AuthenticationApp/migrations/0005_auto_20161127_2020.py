# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-27 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0004_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_professor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
    ]
