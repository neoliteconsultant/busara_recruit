# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20170913_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='requirements',
            field=models.CharField(default='', max_length=12000),
        ),
    ]
