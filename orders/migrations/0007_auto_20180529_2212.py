# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-29 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20180529_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='delivery_date',
            field=models.DateField(verbose_name='Дата доставки'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='delivery_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Стоимость доставки'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='delivery_status',
            field=models.CharField(choices=[('NONE', 'В обработке'), ('CONF', 'Доставка подтверждена'), ('FORM', 'Груз сформирован'), ('DELD', 'В пути'), ('RECD', 'Доставлено'), ('CANC', 'Доставка отменена')], default='NONE', max_length=4, verbose_name='Статус доставки'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Последнее обновление'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_status',
            field=models.CharField(choices=[('WAIT', 'Ожидание оплаты'), ('CONF', 'Оплата подтверждена'), ('CANC', 'Оплата отменена')], default='WAIT', max_length=4, verbose_name='Статус платежа'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Последнее обновление'),
        ),
    ]
