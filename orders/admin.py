from django.contrib import admin
from .models import *


class OrgAddressInline(admin.StackedInline):
    model = OrgAddress
    extra = 1


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0


class DeliveryInline(admin.TabularInline):
    model = Delivery
    extra = 0


class CategoryAdmin(admin.ModelAdmin):  # CATEGORY
    list_display = [field.name for field in Category._meta.fields]

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Address._meta.fields]

    class Meta:
        model = Address


admin.site.register(Address, AddressAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Payment._meta.fields]

    class Meta:
        model = Payment


admin.site.register(Payment, PaymentAdmin)


class DeliveryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Delivery._meta.fields]

    class Meta:
        model = Delivery


admin.site.register(Delivery, DeliveryAdmin)


class BankAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bank._meta.fields]

    class Meta:
        model = Bank


admin.site.register(Bank, BankAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Organization._meta.fields]
    inlines = [OrgAddressInline]

    class Meta:
        model = Organization


admin.site.register(Organization, OrganizationAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.fields]

    class Meta:
        model = Customer


admin.site.register(Customer, CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline, DeliveryInline, PaymentInline]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder


admin.site.register(ProductInOrder, ProductInOrderAdmin)


class AddressCountryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AddressCountry._meta.fields]

    class Meta:
        model = AddressCountry


admin.site.register(AddressCountry, AddressCountryAdmin)


class AddressRegionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AddressRegion._meta.fields]

    class Meta:
        model = AddressRegion


admin.site.register(AddressRegion, AddressRegionAdmin)


class AddressCityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AddressCity._meta.fields]

    class Meta:
        model = AddressCity


admin.site.register(AddressCity, AddressCityAdmin)


class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PaymentType._meta.fields]

    class Meta:
        model = PaymentType


admin.site.register(PaymentType, PaymentTypeAdmin)


class DeliveryTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DeliveryType._meta.fields]

    class Meta:
        model = DeliveryType


admin.site.register(DeliveryType, DeliveryTypeAdmin)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Manufacturer._meta.fields]

    class Meta:
        model = Manufacturer


admin.site.register(Manufacturer, ManufacturerAdmin)


class ProviderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Provider._meta.fields]

    class Meta:
        model = Provider


admin.site.register(Provider, ProviderAdmin)


class StoreAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Store._meta.fields]

    class Meta:
        model = Store


admin.site.register(Store, StoreAdmin)


# Register your models here.
