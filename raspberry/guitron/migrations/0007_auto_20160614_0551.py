# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 05:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guitron', '0006_auto_20160614_0531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='event',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
