# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 06:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('guitron', '0010_auto_20160614_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='event_data',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='guitron.Event'),
            preserve_default=False,
        ),
    ]