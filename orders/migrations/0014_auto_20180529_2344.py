# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-29 20:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20180529_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrgAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_adr_name', models.CharField(max_length=32, verbose_name='Название')),
                ('org_address_address', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_actual_address', to='orders.Address')),
            ],
            options={
                'verbose_name': 'Адрес организации',
                'verbose_name_plural': 'Адреса организаций',
            },
        ),
        migrations.RemoveField(
            model_name='organization',
            name='org_actual_address',
        ),
        migrations.AddField(
            model_name='orgaddress',
            name='org_address_org',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Organization'),
        ),
    ]