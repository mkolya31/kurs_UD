# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-02 22:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0031_auto_20180603_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresscity',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Создан'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addresscity',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
        migrations.AddField(
            model_name='addresscity',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Последнее обновление'),
        ),
        migrations.AddField(
            model_name='addresscountry',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Создан'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addresscountry',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
        migrations.AddField(
            model_name='addresscountry',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Последнее обновление'),
        ),
        migrations.AddField(
            model_name='addressregion',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Создан'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addressregion',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
        migrations.AddField(
            model_name='addressregion',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Последнее обновление'),
        ),
    ]
