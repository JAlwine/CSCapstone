# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 02:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0005_auto_20161127_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_engineer',
            field=models.BooleanField(default=False),
        ),
    ]
