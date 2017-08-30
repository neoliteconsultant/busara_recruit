# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0003_auto_20170829_1016'),
        ('interviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interview',
            name='job_id',
        ),
        migrations.AddField(
            model_name='interview',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='candidates.Candidate'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='interview_date',
            field=models.DateTimeField(),
        ),
    ]
