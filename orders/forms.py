from django import forms
from django.forms import ModelForm
from django.db.models import Q
from .models import *


class CustomersForm(ModelForm):
    c_address = forms.ModelChoiceField(queryset=Address.objects.filter(is_active=True))
    c_organization = forms.ModelChoiceField(queryset=Organization.objects.filter(is_active=True))

    class Meta:
        model = Customer
        fields = ["id", "c_firstname", "c_secondname", "c_phone", "c_email", "c_address", "c_organization",
                  "c_comments"]


class BankForm(ModelForm):
    class Meta:
        model = Bank
        fields = ["bank_name", "bank_BIK", "bank_corr_account"]


class DeliveryForm(ModelForm):
    delivery_order = forms.ModelChoiceField(queryset=Order.objects.filter(is_active=True))
    delivery_type = forms.ModelChoiceField(queryset=DeliveryType.objects.filter(is_active=True))
    delivery_address = forms.ModelChoiceField(queryset=Address.objects.filter(is_active=True))

    class Meta:
        model = Delivery
        fields = ["delivery_order", "delivery_type", "delivery_address", "delivery_date", "delivery_price",
                  "delivery_status"]


class OrderForm(ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.filter(is_active=True))
    store = forms.ModelChoiceField(queryset=Store.objects.filter(is_active=True))
    address = forms.ModelChoiceField(queryset=Address.objects.filter(is_active=True))

    class Meta:
        model = Order
        fields = ["customer", "store", "total_price", "order_status", "comments", "address"]


class CategoryForm(ModelForm):
    cat_parent = forms.ModelChoiceField(queryset=Category.objects.filter(is_active=True))

    class Meta:
        model = Category
        fields = ["cat_name", "cat_parent"]


class CityForm(ModelForm):
    class Meta:
        model = AddressCity
        fields = ["city_name"]


class OrganizationForm(ModelForm):
    org_bank = forms.ModelChoiceField(queryset=Bank.objects.filter(is_active=True))

    class Meta:
        model = Organization
        fields = ["org_type", "org_name", "org_phone", "org_email", "org_website", "org_contact_person", "org_INN",
                  "org_KPP", "org_OGRN", "org_OKPO", "org_checking_account", "org_bank"]


class PaymentForm(ModelForm):
    payment_order = forms.ModelChoiceField(queryset=Order.objects.filter(is_active=True))
    payment_type = forms.ModelChoiceField(queryset=PaymentType.objects.filter(is_active=True))

    class Meta:
        model = Payment
        fields = ["payment_order", "payment_amount", "payment_type", "payment_status"]


class RegionForm(ModelForm):
    class Meta:
        model = AddressRegion
        fields = ["region_name"]


class CountryForm(ModelForm):
    class Meta:
        model = AddressCountry
        fields = ["country_name"]


class ProductForm(ModelForm):
    product_store = forms.ModelChoiceField(queryset=Store.objects.filter(is_active=True))
    product_manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.filter(is_active=True))
    product_category = forms.ModelChoiceField(queryset=Category.objects.filter(is_active=True))
    product_provider = forms.ModelChoiceField(queryset=Provider.objects.filter(is_active=True))

    class Meta:
        model = Product
        fields = ["product_name", "product_article", "product_price", "product_currency", "product_unit", "product_store",
                  "product_manufacturer", "product_category", "product_provider"]


class ProductInOrderForm(ModelForm):
    order = forms.ModelChoiceField(queryset=Order.objects.filter(is_active=True))
    product = forms.ModelChoiceField(queryset=Product.objects.filter(is_active=True))

    class Meta:
        model = ProductInOrder
        fields = ["order", "product", "number", "price_per_item", "total_price"]


class AddressForm(ModelForm):
    address_country = forms.ModelChoiceField(queryset=AddressCountry.objects.filter(is_active=True))
    address_region = forms.ModelChoiceField(queryset=AddressRegion.objects.filter(is_active=True))
    address_city = forms.ModelChoiceField(queryset=AddressCity.objects.filter(is_active=True))

    class Meta:
        model = Address
        fields = ["address_zip", "address_country", "address_region", "address_city", "address_street", "address_house",
                  "address_flat"]


class PaymentTypeForm(ModelForm):
    class Meta:
        model = PaymentType
        fields = ["type_name"]


class DeliveryTypeForm(ModelForm):
    class Meta:
        model = DeliveryType
        fields = ["type_name"]


class ManufacturerForm(ModelForm):
    man_org = forms.ModelChoiceField(queryset=Organization.objects.filter(is_active=True, org_type="MAN"))

    class Meta:
        model = Manufacturer
        fields = ["man_name", "man_org"]


class ProviderForm(ModelForm):
    provider_org = forms.ModelChoiceField(
        queryset=Organization.objects.filter(Q(is_active=True), Q(org_type="MAN") | Q(org_type="PRO")))

    class Meta:
        model = Provider
        fields = ["provider_name", "provider_org"]


class StoreForm(ModelForm):
    store_org = forms.ModelChoiceField(queryset=Organization.objects.filter(is_active=True, org_type="OWN"))

    class Meta:
        model = Store
        fields = ["store_name", "store_org"]
