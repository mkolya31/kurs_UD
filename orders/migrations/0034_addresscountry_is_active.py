# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-02 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0033_remove_addresscountry_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresscountry',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
    ]