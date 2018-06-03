# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-23 22:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_country', models.CharField(blank=True, default=None, max_length=32, null=True)),
                ('address_region', models.CharField(blank=True, default=None, max_length=32, null=True)),
                ('address_city', models.CharField(blank=True, default=None, max_length=32, null=True)),
                ('address_street', models.CharField(max_length=32)),
                ('address_house', models.CharField(max_length=32)),
                ('address_flat', models.CharField(blank=True, default=None, max_length=32, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=128)),
                ('bank_corr_account', models.CharField(max_length=20)),
                ('bank_BIK', models.CharField(max_length=9)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Банк',
                'verbose_name_plural': 'Банки',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=32)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cat_parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Category')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_firstname', models.CharField(max_length=64)),
                ('c_secondname', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('c_email', models.EmailField(max_length=64)),
                ('c_phone', models.CharField(max_length=48)),
                ('c_comments', models.TextField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('c_address', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Address')),
            ],
            options={
                'verbose_name': 'Покупатель',
                'verbose_name_plural': 'Покупатели',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateField()),
                ('delivery_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('delivery_status', models.CharField(choices=[('NONE', 'В обработке'), ('CONF', 'Доставка подтверждена'), ('FORM', 'Груз сформирован'), ('DELD', 'В пути'), ('RECD', 'Доставлено'), ('CANC', 'Доставка отменена')], default='NONE', max_length=4)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('delivery_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Address')),
            ],
            options={
                'verbose_name': 'Доставка',
                'verbose_name_plural': 'Доставки',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('order_status', models.CharField(choices=[('NEW', 'Новый заказ'), ('CONF', 'Заказ сформирован'), ('DELD', 'Доставляется'), ('RECD', 'Выполнен'), ('CANC', 'Заказ отменён')], default='NEW', max_length=4)),
                ('comments', models.TextField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Address')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Customer')),
                ('delivery', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Delivery')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_type', models.CharField(choices=[('NON', 'Не указано'), ('OWN', 'Компания-аватар'), ('MAN', 'Производитель'), ('PRO', 'Поставщик'), ('PRT', 'Компания-партнёр'), ('CLI', 'Компания-клиент')], default='NON', max_length=4)),
                ('org_name', models.CharField(max_length=64)),
                ('org_contact_person', models.CharField(max_length=64)),
                ('org_phone', models.CharField(max_length=48)),
                ('org_INN', models.CharField(blank=True, default=None, max_length=12, null=True)),
                ('org_KPP', models.CharField(blank=True, default=None, max_length=9, null=True)),
                ('org_OGRN', models.CharField(blank=True, default=None, max_length=13, null=True)),
                ('org_OKPO', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('org_checking_account', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('org_actual_address', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_actual_address', to='orders.Address')),
                ('org_bank', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Bank')),
                ('org_legal_address', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_legal_address', to='orders.Address')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('WAIT', 'Ожидание оплаты'), ('CONF', 'Оплата подтверждена'), ('CANC', 'Оплата отменена')], default='WAIT', max_length=4)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('payment_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_order', to='orders.Order')),
            ],
            options={
                'verbose_name': 'Платёж',
                'verbose_name_plural': 'Платежи',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=32)),
                ('product_article', models.CharField(max_length=32)),
                ('product_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Category')),
                ('product_manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_manufacturer', to='orders.Organization')),
                ('product_provider', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_provider', to='orders.Organization')),
                ('product_store', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_store', to='orders.Organization')),
            ],
            options={
                'verbose_name': 'Покупатель',
                'verbose_name_plural': 'Покупатели',
            },
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('price_per_item', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Product')),
            ],
            options={
                'verbose_name': 'Товар в заказе',
                'verbose_name_plural': 'Товары в заказах',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_usage', models.CharField(default=None, max_length=12)),
                ('type_name', models.CharField(default=None, max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Type'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='store',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Organization'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='delivery_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_order', to='orders.Order'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='delivery_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Type'),
        ),
        migrations.AddField(
            model_name='customer',
            name='c_organization',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Organization'),
        ),
    ]