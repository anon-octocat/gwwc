# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 21:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0004_auto_20170730_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pledge',
            name='id',
        ),
        migrations.AlterField(
            model_name='income',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
