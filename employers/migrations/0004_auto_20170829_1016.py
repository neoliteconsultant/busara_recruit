# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0003_auto_20170828_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
