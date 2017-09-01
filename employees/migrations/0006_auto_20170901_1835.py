# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_auto_20170831_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='cover_letter',
            field=models.CharField(default='', max_length=1500),
        ),
        migrations.AlterField(
            model_name='employee',
            name='resume',
            field=models.FileField(default='', upload_to='resume/%Y%m%d/'),
        ),
    ]
