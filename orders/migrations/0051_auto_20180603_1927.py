# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-03 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0050_product_product_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_currency',
            field=models.CharField(choices=[('РУБ', 'RUB'), ('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP')], default='РУБ', max_length=5, verbose_name='Валюта'),
        ),
    ]