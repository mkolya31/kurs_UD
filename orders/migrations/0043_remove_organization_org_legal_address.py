# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-03 12:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0042_auto_20180603_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='org_legal_address',
        ),
    ]