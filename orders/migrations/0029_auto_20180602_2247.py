# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-02 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0028_auto_20180602_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delivery_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.DeliveryType'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.PaymentType'),
        ),
    ]
