# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-04 22:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0019_auto_20161204_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='teacherPhoto',
        ),
    ]
