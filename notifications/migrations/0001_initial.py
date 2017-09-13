# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=150)),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
