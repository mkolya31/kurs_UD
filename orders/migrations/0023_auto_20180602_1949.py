# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-02 16:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_auto_20180602_1948'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['-updated'], 'verbose_name': 'Платёж', 'verbose_name_plural': 'Платежи'},
        ),
    ]