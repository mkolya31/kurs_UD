# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-03 14:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0045_auto_20180603_1621'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ['org_type', 'org_name'], 'verbose_name': 'Организация', 'verbose_name_plural': 'Организации'},
        ),
        migrations.AlterModelOptions(
            name='store',
            options={'verbose_name': 'Магазин', 'verbose_name_plural': 'Магазины'},
        ),
    ]
