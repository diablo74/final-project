# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 06:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guitron', '0011_auto_20160614_0617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='event_data',
        ),
    ]
