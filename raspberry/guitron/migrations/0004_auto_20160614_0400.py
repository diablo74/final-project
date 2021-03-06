# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 04:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('guitron', '0003_auto_20160613_2232'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Data',
        ),
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='group',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='inviter',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='person',
        ),
        migrations.RemoveField(
            model_name='event',
            name='data',
        ),
        migrations.AddField(
            model_name='pin',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 6, 14, 4, 0, 22, 517844, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pin',
            name='pin_id',
            field=models.CharField(default=datetime.datetime(2016, 6, 14, 4, 0, 36, 283592, tzinfo=utc), max_length=256),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='event',
            name='area',
        ),
        migrations.AddField(
            model_name='event',
            name='area',
            field=models.ManyToManyField(to='guitron.Area'),
        ),
        migrations.RemoveField(
            model_name='event',
            name='device',
        ),
        migrations.AddField(
            model_name='event',
            name='device',
            field=models.ManyToManyField(to='guitron.Device'),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
