# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 23:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0010_auto_20161128_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_engineer',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='is_student',
        ),
    ]