# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-03 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0035_auto_20180603_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_alt_id',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=4, verbose_name='Индекс'),
        ),
    ]
