# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 15:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0005_auto_20170829_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='company_logo',
        ),
    ]
