# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-02 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_auto_20180602_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='man_org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Organization'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='provider_org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Organization'),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Organization'),
        ),
    ]