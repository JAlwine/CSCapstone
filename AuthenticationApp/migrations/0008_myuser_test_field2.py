# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0007_myuser_test_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='test_field2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
