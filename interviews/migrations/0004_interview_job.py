# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 06:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20170905_0952'),
        ('interviews', '0003_auto_20170905_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.Job'),
        ),
    ]
