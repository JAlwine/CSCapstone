# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-04 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0017_auto_20161204_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(default=0, upload_to='static/teacherimages'),
        ),
    ]