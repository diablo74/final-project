# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 07:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('guitron', '0019_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='gadget',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='guitron.Status'),
            preserve_default=False,
        ),
    ]
