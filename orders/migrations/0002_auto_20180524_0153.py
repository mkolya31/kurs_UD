# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-23 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='type_usage',
            field=models.CharField(choices=[('PAYM', 'Оплата'), ('DELI', 'Доставка')], default=None, max_length=12),
        ),
    ]