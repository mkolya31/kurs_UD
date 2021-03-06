# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-02 16:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_auto_20180602_1952'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-updated'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='productinorder',
            options={'ordering': ['order'], 'verbose_name': 'Товар в заказе', 'verbose_name_plural': 'Товары в заказах'},
        ),
    ]
