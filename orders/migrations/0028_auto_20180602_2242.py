# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-02 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0027_auto_20180602_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverytype',
            name='type_name',
            field=models.CharField(max_length=32, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='paymenttype',
            name='type_name',
            field=models.CharField(max_length=32, verbose_name='Название'),
        ),
    ]
