from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.core.validators import MinValueValidator, DecimalValidator

IS_ACTIVE = 'Активен'
CREATED = 'Создан'
UPDATED = 'Последнее обновление'


class PaymentType(models.Model):
    type_name = models.CharField('Название', max_length=32)
    is_active = models.BooleanField('Активен', default=True)
    created = models.DateTimeField('Создан', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('Последнее обновление', auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.type_name

    class Meta:
        verbose_name = 'Тип оплаты'
        verbose_name_plural = 'Типы оплаты'


class DeliveryType(models.Model):
    type_name = models.CharField('Название', max_length=32)
    is_active = models.BooleanField('Активен', default=True)
    created = models.DateTimeField('Создан', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('Последнее обновление', auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.type_name

    class Meta:
        verbose_name = 'Тип доставки'
        verbose_name_plural = 'Типы доставки'


class Category(models.Model):
    cat_name = models.CharField('Название', max_length=32)
    cat_parent = models.ForeignKey('self', blank=True, null=True, default=None)
    cat_alt_id = models.DecimalField('Индекс', max_digits=4, decimal_places=0, default=0)
    cat_alt_name = models.CharField('Имя родителя', max_length=32, blank=True, null=True, default=None)
    is_active = models.BooleanField('Активен', default=True)
    created = models.DateTimeField('Создан', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('Последнее обновление', auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.cat_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ["cat_alt_id", "cat_alt_name"]

    def save(self, *args, **kwargs):

        inc = 0
        cat = self
        while cat.cat_parent is not None:
            inc += 1
            cat = cat.cat_parent

        self.cat_alt_id = inc

        if self.cat_parent is None:
            self.cat_alt_name = ""
        else:
            self.cat_alt_name = self.cat_parent.cat_name

        super(Category, self).save(*args, **kwargs)


class AddressCountry(models.Model):
    country_name = models.CharField('Страна', max_length=32, blank=True, null=True, default=None)
    is_active = models.BooleanField('Активен', default=True)
    created = models.DateTimeField('Создан', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('Последнее обновление', auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.country_name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class AddressRegion(models.Model):
    region_name = models.CharField('Регион', max_length=32, blank=True, null=True, default=None)
    is_active = models.BooleanField('Активен', default=True)
    created = models.DateTimeField('Создан', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('Последнее обновление', auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.region_name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class AddressCity(models.Model):
    city_name = models.CharField('Город', max_length=32, blank=True, null=True, default=None)
    is_active = models.BooleanField('Активен', default=True)
    created = models.DateTimeField('Создан', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('Последнее обновление', auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.city_name

    class Meta:
        verbose_name = 'Населённый пункт'
        verbose_name_plural = 'Города и населённые пункты'


class Address(models.Model):
    address_zip = models.CharField('Индекс', max_length=32, blank=True, null=True, default=None)
    address_country = models.ForeignKey(AddressCountry, blank=True, null=True, default=None)
    address_region = models.ForeignKey(AddressRegion, blank=True, null=True, default=None)
    address_city = models.ForeignKey(AddressCity, blank=True, null=True, default=None)
    address_street = models.CharField('Улица', max_length=64)
    address_house = models.CharField('Дом', max_length=32)
    address_flat = models.CharField('Квартира', max_length=16, blank=True, null=True, default=None)
    used = models.BooleanField('Используется', default=False)
    is_active = models.BooleanField('Активен', default=True)
    created = models.DateTimeField('Создан', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('Последнее обновление', auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.address_street, self.address_house)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Payment(models.Model):
    WAITING_FOR_PAYMENT = 'Ожидание'
    CONFIRMED = 'Подтверждена'
    CANCEL = 'Отмена'
    PAID_STATUSES = (
        (WAITING_FOR_PAYMENT, 'Ожидание оплаты'),
        (CONFIRMED, 'Оплата подтверждена'),
        (CANCEL, 'Оплата отменена'),
    )

    payment_order = models.ForeignKey('Order', related_name='payment_order')
    payment_type = models.ForeignKey(PaymentType)
    payment_amount = models.DecimalField('Размер платежа', max_digits=10, decimal_places=2, default=0,
                                         validators=[MinValueValidator(0, "Введите положительное число"),
                                                     DecimalValidator(10, 2)])
    payment_status = models.CharField('Статус платежа', max_length=12, choices=PAID_STATUSES,
                                      default=WAITING_FOR_PAYMENT)
    is_active = models.BooleanField('Активен', default=True)
    created = models.DateTimeField('Создан', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('Последнее обновление', auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Платёж №%s заказ №%s" % (self.id, self.payment_order_id)

    class Meta:
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'
        ordering = ["-created"]


class Delivery(models.Model):
    NONE = 'В обработке'
    CONFIRMED = 'Подтверждён'
    FORMED = 'Сформирован'
    DELIVERED = 'Доставляется'
    RECEIVED = 'Доставлено'
    CANCEL = 'Отмена'
    DELIVERY_STATUSES = (
        (NONE, 'В обработке'),
        (CONFIRMED, 'Доставка подтверждена'),
        (FORMED, 'Груз сформирован'),
        (DELIVERED, 'В пути'),
        (RECEIVED, 'Доставлено'),
        (CANCEL, 'Доставка отменена'),
    )

    delivery_order = models.ForeignKey('Order', related_name='delivery_order')
    delivery_type = models.ForeignKey(DeliveryType)
    delivery_address = models.ForeignKey(Address)
    delivery_date = models.DateField('Дата доставки', blank=False)
    delivery_price = models.DecimalField('Стоимость доставки', max_digits=10, decimal_places=2, default=0,
                                         validators=[MinValueValidator(0, "Введите положительное число"),
                                                     DecimalValidator(10, 2)])
    delivery_status = models.CharField('Статус доставки', max_length=12, choices=DELIVERY_STATUSES, default=NONE)
    is_active = models.BooleanField(IS_ACTIVE, default=True)
    created = models.DateTimeField(CREATED, auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(UPDATED, auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Доставка №%s заказ №%s" % (self.id, self.delivery_order_id)

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'
        ordering = ["-updated"]


class Bank(models.Model):
    bank_name = models.CharField('Название', max_length=128)
    bank_corr_account = models.CharField('Корреспондентский счёт', max_length=20)
    bank_BIK = models.CharField('БИК', max_length=9)
    is_active = models.BooleanField(IS_ACTIVE, default=True)
    created = models.DateTimeField(CREATED, auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(UPDATED, auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Банк %s" % self.bank_name

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'
        ordering = ["bank_name"]


class Organization(models.Model):
    NONE = 'NON'
    OWN = 'OWN'
    MANUFACTURER = 'MAN'
    PROVIDER = 'PRO'
    PARTNER = 'PRT'
    CLIENT = 'CLI'
    ORG_TYPES = (
        (NONE, 'Не указано'),
        (OWN, 'Компания-аватар'),
        (MANUFACTURER, 'Производитель'),
        (PROVIDER, 'Поставщик'),
        (PARTNER, 'Компания-партнёр'),
        (CLIENT, 'Компания-клиент'),
    )

    org_type = models.CharField('Тип организации', max_length=4, choices=ORG_TYPES, default=NONE)
    org_name = models.CharField('Название', max_length=64)
    org_phone = models.CharField('Телефон', max_length=48)
    org_email = models.CharField('E-mail', max_length=48, blank=True, null=True, default=None)
    org_website = models.CharField('Сайт', max_length=48, blank=True, null=True, default=None)
    org_contact_person = models.CharField('Контактное лицо', max_length=64, blank=True, null=True, default=None)
    org_INN = models.CharField('ИНН', max_length=12, blank=True, null=True, default=None)
    org_KPP = models.CharField('КПП', max_length=9, blank=True, null=True, default=None)
    org_OGRN = models.CharField('ОРГН', max_length=13, blank=True, null=True, default=None)
    org_OKPO = models.CharField('ОКПО', max_length=10, blank=True, null=True, default=None)
    org_checking_account = models.CharField('Расчётный счёт', max_length=20, blank=True, null=True, default=None)
    org_bank = models.ForeignKey(Bank, blank=True, null=True, default=None)
    is_active = models.BooleanField(IS_ACTIVE, default=True)
    created = models.DateTimeField(CREATED, auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(UPDATED, auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.org_type, self.org_name)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class Manufacturer(models.Model):
    man_name = models.CharField('Название', max_length=64)
    man_org = models.ForeignKey(Organization)
    is_active = models.BooleanField(IS_ACTIVE, default=True)
    created = models.DateTimeField(CREATED, auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(UPDATED, auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.man_name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
        ordering = ["man_name"]


class Provider(models.Model):
    provider_name = models.CharField('Название', max_length=64)
    provider_org = models.ForeignKey(Organization)
    is_active = models.BooleanField(IS_ACTIVE, default=True)
    created = models.DateTimeField(CREATED, auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(UPDATED, auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.provider_name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ["provider_name"]


class Store(models.Model):
    store_name = models.CharField('Название', max_length=64)
    store_org = models.ForeignKey(Organization)
    is_active = models.BooleanField(IS_ACTIVE, default=True)
    created = models.DateTimeField(CREATED, auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(UPDATED, auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.store_name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class OrgAddress(models.Model):
    org_adr_name = models.CharField('Название', max_length=32)
    org_adr_org = models.ForeignKey(Organization, blank=True, null=True, default=None)
    org_adr_address = models.ForeignKey(Address, related_name='org_actual_address', blank=True, null=True,
                                        default=None)
    is_active = models.BooleanField('Активен', default=True)
    created = models.DateTimeField('Создан', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('Последнее обновление', auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.org_adr_org.org_name, self.org_adr_name)

    class Meta:
        verbose_name = 'Адрес организации'
        verbose_name_plural = 'Адреса организаций'


class CustomerAddress(models.Model):
    adr_name = models.CharField('Название', max_length=32)
    adr_customer = models.ForeignKey('Customer', related_name="adr_customer", blank=True, null=True, default=None)
    adr_address = models.ForeignKey(Address, related_name='adr_address', blank=True, null=True, default=None)
    is_active = models.BooleanField('Активен', default=True)
    created = models.DateTimeField('Создан', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('Последнее обновление', auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.adr_customer.c_secondname, self.adr_name)

    class Meta:
        verbose_name = 'Адрес покупателя'
        verbose_name_plural = 'Адреса покупателей'


class Customer(models.Model):
    c_firstname = models.CharField('Имя', max_length=64)
    c_secondname = models.CharField(max_length=64, blank=True, null=True, default=None)
    c_email = models.EmailField('E-mail', max_length=64)
    c_phone = models.CharField('Телефон', max_length=48)
    c_organization = models.ForeignKey(Organization, blank=True, null=True, default=None)
    c_comments = models.TextField('Комментарий', blank=True, null=True, default=None)
    is_active = models.BooleanField(IS_ACTIVE, default=True)
    created = models.DateTimeField(CREATED, auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(UPDATED, auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Покупатель %s %s" % (self.c_secondname, self.id)

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
        ordering = ["c_firstname"]


class Currency(models.Model):
    currency_name = models.CharField('Валюта', max_length=32, blank=True, null=True, default=None)
    currency_value = models.DecimalField('Курс к рублю', max_digits=5, decimal_places=2, default=0,
                                         validators=[MinValueValidator(0, "Введите положительное число"),
                                                     DecimalValidator(5, 2)])
    is_active = models.BooleanField('Активен', default=True)
    created = models.DateTimeField('Создан', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('Последнее обновление', auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.currency_name

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'


class Product(models.Model):
    NONE = 'NON'
    SQUARE_METER = 'м²'
    RUNNING_METER = 'м. пог.'
    UNIT = 'Шт.'
    PACKING = 'Уп.'
    PRODUCT_UNIT = (
        (NONE, 'Не указано'),
        (SQUARE_METER, 'м²'),
        (RUNNING_METER, 'м. пог.'),
        (UNIT, 'шт.'),
        (PACKING, 'упак.'),
    )

    product_name = models.CharField('Название', max_length=64)
    product_article = models.CharField('Артикл', max_length=32)
    product_price = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0,
                                        validators=[MinValueValidator(0, "Введите положительное число"),
                                                    DecimalValidator(10, 2)])
    product_currency = models.ForeignKey(Currency, blank=True, null=True, default=None)
    product_unit = models.CharField('Единица измерения', max_length=10, choices=PRODUCT_UNIT, default=NONE)
    product_store = models.ForeignKey(Store, related_name='product_store', blank=True, null=True, default=None)
    product_manufacturer = models.ForeignKey(Manufacturer, related_name='product_manufacturer')
    product_category = models.ForeignKey(Category)
    product_provider = models.ForeignKey(Provider, related_name='product_provider', blank=True, null=True, default=None)
    is_active = models.BooleanField(IS_ACTIVE, default=True)
    created = models.DateTimeField(CREATED, auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(UPDATED, auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.product_name, self.product_article)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ["product_manufacturer"]


class Order(models.Model):
    NEW = '1. Новый'
    CONFIRMED = '2 .Подтверждён'
    DELIVERED = '3. Доставляется'
    RECEIVED = '4. Выполнен'
    CANCEL = '5. Отменён'
    ERROR = '6. Ошибка'
    ORDER_STATUSES = (
        (NEW, 'Новый заказ'),
        (CONFIRMED, 'Заказ сформирован'),
        (DELIVERED, 'Доставляется'),
        (RECEIVED, 'Выполнен'),
        (CANCEL, 'Заказ отменён'),
        (ERROR, 'Ошибка заказа'),
    )

    created = models.DateTimeField('Дата создания', auto_now_add=True, auto_now=False)
    customer = models.ForeignKey(Customer)
    store = models.ForeignKey(Store, blank=True, null=True, default=None)
    order_NDS = models.DecimalField('Сумма НДС', max_digits=10, decimal_places=2,
                                    default=0, validators=[MinValueValidator(0, "Введите положительное число"),
                                                           DecimalValidator(10, 2)])
    total_product_price = models.DecimalField('Итоговая стоимость(без доставки)', max_digits=10, decimal_places=2,
                                              default=0,
                                              validators=[MinValueValidator(0, "Введите положительное число"),
                                                          DecimalValidator(10, 2)])  # total price for all products
    total_delivery_price = models.DecimalField('Стоимость доставки', max_digits=10, decimal_places=2,
                                               default=0,
                                               validators=[MinValueValidator(0, "Введите положительное число"),
                                                           DecimalValidator(10, 2)])
    balance = models.DecimalField('Баланс заказа', max_digits=10, decimal_places=2,
                                  default=0, validators=[DecimalValidator(10, 2)])
    order_total_amount = models.DecimalField('Итоговая стоимость', max_digits=10, decimal_places=2,
                                             default=0, validators=[MinValueValidator(0, "Введите положительное число"),
                                                                    DecimalValidator(10, 2)])
    order_status = models.CharField('Статус заказа', max_length=16, choices=ORDER_STATUSES, default=NEW)
    comments = models.TextField('Комментарий', blank=True, null=True, default=None)
    is_active = models.BooleanField(IS_ACTIVE, default=True)
    updated = models.DateTimeField(UPDATED, auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.store.store_name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ["order_status", "-created"]


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    number = models.IntegerField('Количество', default=1)
    NDS_amount = models.DecimalField('Сумма НДС', max_digits=10, decimal_places=2, default=0)
    price_per_item = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField('Итоговая стоимость', max_digits=10, decimal_places=2,
                                      default=0)  # price*nmb*discount
    is_active = models.BooleanField(IS_ACTIVE, default=True)
    created = models.DateTimeField(CREATED, auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(UPDATED, auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.product.product_name, self.product.id)

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказах'
        ordering = ["order"]

    def save(self, *args, **kwargs):
        price_per_item = self.product.product_price
        price_per_item *= self.product.product_currency.currency_value
        self.price_per_item = price_per_item
        self.total_price = self.number * price_per_item
        self.NDS_amount = self.total_price / 100 * 18

        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
    all_delivery_in_order = Delivery.objects.filter(delivery_order=order, is_active=True)
    all_payments_in_order = Payment.objects.filter(payment_order=order, is_active=True)

    delivery_total_price = 0
    order_total_price = 0
    order_payment = 0

    del_flag = False
    del_comp_flag = True

    for item in all_products_in_order:
        order_total_price += item.total_price

    for item in all_delivery_in_order:
        delivery_total_price += item.delivery_price

        if item.delivery_status != 'Доставлено':
            del_comp_flag = False

        if item.delivery_status == 'Доставляется':
            del_flag = True

    for item in all_payments_in_order:
        if item.payment_status == 'Подтверждена':
            order_payment += item.payment_amount

    instance.order.total_delivery_price = delivery_total_price
    instance.order.total_product_price = order_total_price
    instance.order.order_total_amount = order_total_price + delivery_total_price
    instance.order.order_NDS = (order_total_price / 100 * 18)
    instance.order.balance = order_total_price + delivery_total_price - order_payment

    if instance.order.balance == 0 and all_payments_in_order.count() > 0:
        instance.order.order_status = '2. Подтверждён'
        if del_flag:
            instance.order.order_status = '3. Доставляется'
        if del_comp_flag:
            instance.order.order_status = '4. Выполнен'

    elif instance.order.balance < 0:
        instance.order.order_status = '6. Ошибка'

    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)


def delivery_post_save(sender, instance, created, **kwargs):
    order = instance.delivery_order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
    all_delivery_in_order = Delivery.objects.filter(delivery_order=order, is_active=True)
    all_payments_in_order = Payment.objects.filter(payment_order=order, is_active=True)

    delivery_total_price = 0
    order_total_price = 0
    order_payment = 0

    del_flag = False
    del_comp_flag = True

    for item in all_products_in_order:
        order_total_price += item.total_price

    for item in all_delivery_in_order:
        delivery_total_price += item.delivery_price

        if item.delivery_status != 'Доставлено':
            del_comp_flag = False

        if item.delivery_status == 'Доставляется':
            del_flag = True

    for item in all_payments_in_order:
        if item.payment_status == 'Подтверждена':
            order_payment += item.payment_amount

    instance.delivery_order.total_delivery_price = delivery_total_price
    instance.delivery_order.total_product_price = order_total_price
    instance.delivery_order.order_total_amount = order_total_price + delivery_total_price
    instance.delivery_order.order_NDS = (order_total_price / 100 * 18)
    instance.delivery_order.balance = order_total_price + delivery_total_price - order_payment

    if instance.delivery_order.balance == 0 and all_payments_in_order.count() > 0:
        instance.delivery_order.order_status = '2. Подтверждён'
        if del_flag:
            instance.delivery_order.order_status = '3. Доставляется'
        if del_comp_flag:
            instance.delivery_order.order_status = '4. Выполнен'

    elif instance.delivery_order.balance < 0:
        instance.delivery_order.order_status = '6. Ошибка'

    instance.delivery_order.save(force_update=True)


post_save.connect(delivery_post_save, sender=Delivery)


def payment_post_save(sender, instance, created, **kwargs):
    order = instance.payment_order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
    all_delivery_in_order = Delivery.objects.filter(delivery_order=order, is_active=True)
    all_payments_in_order = Payment.objects.filter(payment_order=order, is_active=True)

    delivery_total_price = 0
    order_total_price = 0
    order_payment = 0

    del_flag = False
    del_comp_flag = True

    for item in all_products_in_order:
        order_total_price += item.total_price

    for item in all_delivery_in_order:
        delivery_total_price += item.delivery_price

        if item.delivery_status != 'Доставлено':
            del_comp_flag = False

        if item.delivery_status == 'Доставляется':
            del_flag = True

    for item in all_payments_in_order:
        if item.payment_status == 'Подтверждена':
            order_payment += item.payment_amount

    instance.payment_order.total_delivery_price = delivery_total_price
    instance.payment_order.total_product_price = order_total_price
    instance.payment_order.order_total_amount = order_total_price + delivery_total_price
    instance.payment_order.order_NDS = (order_total_price / 100 * 18)
    instance.payment_order.balance = order_total_price + delivery_total_price - order_payment

    if instance.payment_order.balance == 0 and all_payments_in_order.count() > 0:
        instance.payment_order.order_status = '2. Подтверждён'
        if del_flag:
            instance.payment_order.order_status = '3. Доставляется'
        if del_comp_flag:
            instance.payment_order.order_status = '4. Выполнен'

    elif instance.payment_order.balance < 0:
        instance.payment_order.order_status = '6. Ошибка'

    instance.payment_order.save(force_update=True)


post_save.connect(payment_post_save, sender=Payment)


# def order_post_save(sender, instance, created, **kwargs):
#     order = instance
#     all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
#     all_delivery_in_order = Delivery.objects.filter(delivery_order=order, is_active=True)
#     all_payments_in_order = Payment.objects.filter(payment_order=order, is_active=True)
#
#     delivery_total_price = 0
#     order_total_price = 0
#     order_payment = 0
#
#     for item in all_products_in_order:
#         order_total_price += item.total_price
#
#     for item in all_delivery_in_order:
#         delivery_total_price += item.delivery_price
#
#     for item in all_payments_in_order:
#         order_payment += item.payment_amount
#
#     instance.total_price = order_total_price + delivery_total_price
#     instance.order_NDS = (order_total_price / 100 * 18)
#     instance.balance = order_total_price - order_payment
#
#     instance.save(force_update=True)
#
#
# post_save.connect(order_post_save, sender=Order)


def customer_address_post_save(sender, instance, created, **kwargs):
    instance.adr_address.used = True
    instance.adr_address.save()


post_save.connect(customer_address_post_save, sender=CustomerAddress)


def org_address_post_save(sender, instance, created, **kwargs):
    instance.org_adr_address.used = True
    instance.org_adr_address.save()


post_save.connect(org_address_post_save, sender=OrgAddress)


# def customer_address_pre_delete(sender, instance, created, **kwargs):
#
#     print("Pre delete")
#     instance.adr_address.used = False
#     instance.adr_address.save()
#
#
# pre_delete.connect(customer_address_pre_delete, sender=CustomerAddress)
