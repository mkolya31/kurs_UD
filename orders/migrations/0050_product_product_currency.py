# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-03 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0049_auto_20180603_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_currency',
            field=models.CharField(choices=[('РУБ', 'Не указано'), ('USD', 'За м²'), ('EUR', 'За м. пог.'), ('GBP', 'За штуку')], default='РУБ', max_length=5, verbose_name='Валюта'),
        ),
    ]
