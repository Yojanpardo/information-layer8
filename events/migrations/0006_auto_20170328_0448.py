# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20170327_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_end',
            field=models.CharField(default='2017-05-04 12:00:00', max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_start',
            field=models.CharField(default='2017-05-04 12:00:00', max_length=255),
        ),
    ]
