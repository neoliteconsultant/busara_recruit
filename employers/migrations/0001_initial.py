# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-08-25 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField()),
            ],
        ),
    ]