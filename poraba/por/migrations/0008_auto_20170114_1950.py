# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-14 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('por', '0007_auto_20170114_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='st_vozil',
        ),
        migrations.AddField(
            model_name='profile',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
    ]