# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-29 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20180529_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='org_actual_address',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_actual_address', to='orders.Address'),
        ),
    ]
