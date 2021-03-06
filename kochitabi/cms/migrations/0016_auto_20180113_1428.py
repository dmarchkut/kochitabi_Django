# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-13 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0015_auto_20180113_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinate',
            name='latitude',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='緯度'),
        ),
        migrations.AlterField(
            model_name='coordinate',
            name='longitude',
            field=models.FloatField(blank=True, max_length=11, null=True, verbose_name='経度'),
        ),
    ]
