# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-30 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0002_auto_20160530_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='gnd_id',
            field=models.CharField(blank=True, help_text='GND id of Institution.', max_length=255),
        ),
        migrations.AddField(
            model_name='institution',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=12, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=12, max_digits=20, null=True),
        ),
    ]
