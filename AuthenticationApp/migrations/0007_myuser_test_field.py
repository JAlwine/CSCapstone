# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0006_auto_20161127_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='test_field',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
