# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 19:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('por', '0008_auto_20170114_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='grade',
        ),
    ]
