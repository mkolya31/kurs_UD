# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-03 13:21
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0044_auto_20180603_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delivery_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0, 'Введите положительное число'), django.core.validators.DecimalValidator(10, 2)], verbose_name='Стоимость доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0, 'Введите положительное число'), django.core.validators.DecimalValidator(10, 2)], verbose_name='Итоговая стоимость'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0, 'Введите положительное число'), django.core.validators.DecimalValidator(10, 2)], verbose_name='Размер платежа'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0, 'Введите положительное число'), django.core.validators.DecimalValidator(10, 2)], verbose_name='Цена'),
        ),
    ]
