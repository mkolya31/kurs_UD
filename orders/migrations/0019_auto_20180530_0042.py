# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-29 21:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20180530_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='address_city1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.AddressCity'),
        ),
        migrations.AddField(
            model_name='address',
            name='address_country1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.AddressCountry'),
        ),
        migrations.AddField(
            model_name='address',
            name='address_region1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.AddressRegion'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_city',
            field=models.CharField(blank=True, default=None, max_length=48, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_country',
            field=models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_region',
            field=models.CharField(blank=True, default=None, max_length=48, null=True, verbose_name='Регион'),
        ),
    ]
