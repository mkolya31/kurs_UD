# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-03 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0046_auto_20180603_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_store',
            field=models.ForeignKey(blank=True, default='Любой', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_store', to='orders.Store'),
        ),
    ]
