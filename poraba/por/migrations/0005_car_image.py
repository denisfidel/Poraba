# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('por', '0004_auto_20170108_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cars'),
        ),
    ]
