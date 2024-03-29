# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20170829_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='availability',
            field=models.CharField(choices=[('Fulltime', 'Fulltime'), ('Part time', 'Part time')], default='Fulltime', max_length=30),
        ),
        migrations.AddField(
            model_name='job',
            name='benefits',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='job',
            name='industry',
            field=models.CharField(choices=[('Any', 'Any'), ('Accounting', 'Accounting'), ('Customer Service', 'Customer Service'), ('Government', 'Government'), ('Education', 'Education'), ('Engineering', 'Engineering'), ('Hospitality', 'Hospitality'), ('Healthcare', 'Healthcare'), ('Farming and Agriculture', 'Farming and Agriculture'), ('IT and Telecoms', 'IT and Telecoms'), ('Legal', 'Legal'), ('Security', 'Security'), ('Other', 'Other')], default='Any', max_length=30),
        ),
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
    ]
