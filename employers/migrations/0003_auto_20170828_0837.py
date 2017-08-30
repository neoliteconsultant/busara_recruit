# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0002_auto_20170827_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='user',
        ),
        migrations.AddField(
            model_name='employer',
            name='company_logo',
            field=models.ImageField(blank=True, upload_to='employers'),
        ),
        migrations.AddField(
            model_name='employer',
            name='email',
            field=models.CharField(default='', max_length=35),
        ),
        migrations.AddField(
            model_name='employer',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='employer',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='employer',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='employer',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='employer',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='employer',
            name='company_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]