# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 03:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('guitron', '0022_light'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='signal',
            field=models.CharField(default=datetime.datetime(2016, 6, 15, 3, 25, 0, 457695, tzinfo=utc), max_length=256),
            preserve_default=False,
        ),
    ]
