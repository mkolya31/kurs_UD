# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-03 00:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0038_auto_20180603_0327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['cat_alt_name', 'cat_alt_id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]