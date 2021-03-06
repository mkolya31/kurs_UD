# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-29 22:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20180530_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Delivery'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Payment'),
        ),
    ]
