# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 07:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20170828_0932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='employer_id',
            new_name='employer',
        ),
    ]