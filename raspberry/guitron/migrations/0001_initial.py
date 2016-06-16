# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-13 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=256)),
                ('time_date', models.TextField()),
                ('location', models.TextField()),
                ('area_id', models.TextField()),
                ('event_data', models.CharField(max_length=256)),
            ],
        ),
    ]