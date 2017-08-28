# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-08-26 21:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employers', '0002_auto_20170827_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('requirements', models.CharField(max_length=1000)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('employer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employers.Employer')),
            ],
        ),
    ]
