# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-14 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('por', '0006_auto_20170110_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='por.Profile'),
        ),
    ]
