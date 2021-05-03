# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 12:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employers', '0008_remove_employer_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='username',
        ),
        migrations.AddField(
            model_name='employer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
