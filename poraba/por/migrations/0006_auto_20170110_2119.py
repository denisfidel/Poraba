# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('por', '0005_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='kilometers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cars/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]