from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required


@login_required
def home_page(request):
    return render(request, "home.html", locals())


@login_required
def view_profile(request):
    username = auth.get_user(request).username
    args = {
        'user': request.user
    }

    return render(request, 'login_auth/view_profile.html', locals())


# CUSTOMER
@login_required
def customer_out(request):
    client_list = Customer.objects.filter(is_active=True)
    return render(request, "Customer/customerout.html", locals())


@login_required
def customer_view(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    return render(request, "Customer/customerview.html", locals())


@login_required
def customer_add(request):
    form = CustomersForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../../../customer")
        else:
            return render(request, "Customer/customerout.html", locals())
    return render(request, "Customer/customeradd.html", locals())


@login_required
def customer_edit(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    form = CustomersForm(instance=customer)
    if request.method == "POST":
        form = CustomersForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("../../../customer")
        else:
            return render(request, "Customer/customerout.html", locals())
    return render(request, "Customer/customeredit.html", locals())


@login_required
def customer_delete(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    if request.method == "POST":
        print(request.POST)
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            customer.is_active = False
            customer.save()
            return redirect("../../../customer")
        else:
            return redirect("../../../customer")
    return render(request, "Customer/customerdelete.html")


# ADDRESS
@login_required
def address_out(request):
    address_list = Address.objects.filter(is_active=True)
    address_verbose = Address._meta.verbose_name_plural
    return render(request, "Address/address_out.html", locals())


@login_required
def address_add(request):
    form = AddressForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../../../address")
        else:
            return render(request, "Address/address_out.html", locals())
    return render(request, "Address/address_add.html", locals())


@login_required
def address_edit(request, address_id):
    address = Address.objects.get(id=address_id)
    form = AddressForm(instance=address)
    if request.method == "POST":
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect("../../../address")
        else:
            return render(request, "Address/address_out.html", locals())
    return render(request, "Address/address_edit.html", locals())


@login_required
def address_delete(request, address_id):
    address = Address.objects.get(id=address_id)
    if request.method == "POST":
        print(request.POST)
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            address.is_active = False
            address.save()
            return redirect("../../../address")
        else:
            return redirect("../../../address")
    return render(request, "Address/address_delete.html", locals())


# BANKS
@login_required
def bank_out(request):
    bank_list = Bank.objects.filter(is_active=True)
    bank_verbose = Bank._meta.verbose_name_plural
    return render(request, "Bank/bank_out.html", locals())


@login_required
def bank_add(request):
    form = BankForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../../../bank")
        else:
            return redirect("../../../bank")
    return render(request, "Bank/bank_add.html", locals())


@login_required
def bank_edit(request, bank_id):
    bank = Bank.objects.get(id=bank_id)
    form = BankForm(instance=bank)
    if request.method == "POST":
        form = BankForm(request.POST, instance=bank)
        if form.is_valid():
            form.save()
            return redirect("../../../bank")
        else:
            return redirect("../../../bank")
    return render(request, "Bank/bank_edit.html", locals())


@login_required
def bank_delete(request, bank_id):
    bank = Bank.objects.get(id=bank_id)
    if request.method == "POST":
        print(request.POST)
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            bank.is_active = False
            bank.save()
            return redirect("../../../bank")
        else:
            return redirect("../../../bank")
    return render(request, "Bank/bank_delete.html", locals())


# DELIVERY
@login_required
def delivery_out(request):
    delivery_list = Delivery.objects.filter(is_active=True)
    delivery_verbose = Delivery._meta.verbose_name_plural
    return render(request, "Delivery/delivery_out.html", locals())


@login_required
def delivery_add(request):
    form = DeliveryForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../../../delivery")
        else:
            return redirect("../../../delivery")
    return render(request, "Delivery/delivery_add.html", locals())


@login_required
def delivery_edit(request, delivery_id):
    delivery = Delivery.objects.get(id=delivery_id)
    form = DeliveryForm(instance=delivery)
    if request.method == "POST":
        form = DeliveryForm(request.POST, instance=delivery)
        if form.is_valid():
            form.save()
            return redirect("../../../delivery")
        else:
            return redirect("../../../delivery")
    return render(request, "Delivery/delivery_edit.html", locals())


@login_required
def delivery_delete(request, delivery_id):
    delivery = Delivery.objects.get(id=delivery_id)
    if request.method == "POST":
        print(request.POST)
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            delivery.is_active = False
            delivery.save()
            return redirect("../../../delivery")
        else:
            return redirect("../../../delivery")
    return render(request, "Delivery/delivery_delete.html", locals())


# ORDERS
@login_required
def order_out(request):
    order_list = Order.objects.filter(is_active=True)
    order_verbose = Order._meta.verbose_name_plural
    return render(request, "Order/order_out.html", locals())


def order_view(request, order_id):
    order = Order.objects.get(id=order_id)
    order_verbose = Order._meta.verbose_name
    products_list = ProductInOrder.objects.filter(order=order)
    delivery_list = Delivery.objects.filter(delivery_order=order)
    payment_list = Payment.objects.filter(payment_order=order)
    return render(request, "Order/order_view.html", locals())


@login_required
def order_add(request):
    form = NewOrderForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../../../order")
        else:
            return redirect("../../../order")
    return render(request, "Order/order_add.html", locals())


@login_required
def order_edit(request, order_id):
    order = Order.objects.get(id=order_id)
    form = EditOrderForm(instance=order)
    if request.method == "POST":
        form = EditOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("../../../order")
        else:
            return redirect("../../../order")
    return render(request, "Order/order_edit.html", locals())


@login_required
def order_delete(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == "POST":
        print(request.POST)
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            order.is_active = False
            order.save()
            return redirect("../../../order")
        else:
            return redirect("../../../order")
    return render(request, "Order/order_delete.html", locals())


# CATEGORIES
@login_required
def category_out(request):
    category_list = Category.objects.filter(is_active=True)
    category_verbose = Category._meta.verbose_name_plural
    return render(request, "Category/category_out.html", locals())


@login_required
def category_add(request):
    form = CategoryForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../../../category")
        else:
            return redirect("../../../category")
    return render(request, "Category/category_add.html", locals())


@login_required
def category_edit(request, category_id):
    category = Category.objects.get(id=category_id)
    form = CategoryForm(instance=category)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("../../../category")
        else:
            return redirect("../../../category")
    return render(request, "Category/category_edit.html", locals())


@login_required
def category_delete(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        print(request.POST)
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            category.is_active = False
            category.save()
            return redirect("../../../category")
        else:
            return redirect("../../../category")
    return render(request, "Category/category_delete.html", locals())


# CITY
@login_required
def city_out(request):
    city_list = AddressCity.objects.filter(is_active=True)
    city_verbose = AddressCity._meta.verbose_name_plural
    return render(request, "City/city_out.html", locals())


@login_required
def city_add(request):
    form = CityForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../../../city")
        else:
            return redirect("../../../city")
    return render(request, "City/city_add.html", locals())


@login_required
def city_edit(request, city_id):
    city = AddressCity.objects.get(id=city_id)
    form = CityForm(instance=city)
    if request.method == "POST":
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect("../../../city")
        else:
            return redirect("../../../city")
    return render(request, "City/city_edit.html", locals())


@login_required
def city_delete(request, city_id):
    city = AddressCity.objects.get(id=city_id)
    if request.method == "POST":
        print(request.POST)
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            city.is_active = False
            city.save()
            return redirect("../../../city")
        else:
            return redirect("../../../city")
    return render(request, "City/city_delete.html", locals())


# ORGANIZATION
@login_required
def organization_out(request):
    organization_list = Organization.objects.filter(is_active=True)
    organization_verbose = Organization._meta.verbose_name_plural
    return render(request, "Organization/organization_out.html", locals())


@login_required
def organization_add(request):
    form = OrganizationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../../../organization")
        else:
            return redirect("../../../organization")
    return render(request, "Organization/organization_add.html", locals())


@login_required
def organization_edit(request, organization_id):
    organization = Organization.objects.get(id=organization_id)
    form = OrganizationForm(instance=organization)
    if request.method == "POST":
        form = OrganizationForm(request.POST, instance=organization)
        if form.is_valid():
            form.save()
            return redirect("../../../organization")
        else:
            return redirect("../../../organization")
    return render(request, "Organization/organization_edit.html", locals())


@login_required
def organization_delete(request, organization_id):
    organization = Organization.objects.get(id=organization_id)
    if request.method == "POST":
        print(request.POST)
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            organization.is_active = False
            organization.save()
            return redirect("../../../organization")
        else:
            return redirect("../../../organization")
    return render(request, "Organization/organization_delete.html", locals())


# PAYMENT
@login_required
def payment_out(request):
    payment_list = Payment.objects.filter(is_active=True)
    payment_verbose = Payment._meta.verbose_name_plural
    return render(request, "Payment/payment_out.html", locals())


@login_required
def payment_add(request):
    form = PaymentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../../../payment")
        else:
            return redirect("../../../payment")
    return render(request, "Payment/payment_add.html", locals())


@login_required
def payment_edit(request, payment_id):
    payment = Payment.objects.get(id=payment_id)
    form = PaymentForm(instance=payment)
    if request.method == "POST":
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect("../../../payment")
        else:
            return redirect("../../../payment")
    return render(request, "Payment/payment_edit.html", locals())


@login_required
def payment_delete(request, payment_id):
    payment = Payment.objects.get(id=payment_id)
    if request.method == "POST":
        print(request.POST)
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            payment.is_active = False
            payment.save()
            return redirect("../../../payment")
        else:
            return redirect("../../../payment")
    return render(request, "Payment/payment_delete.html", locals())


# REGION
@login_required
def region_out(request):
    region_list = AddressRegion.objects.filter(is_active=True)
    region_verbose = AddressRegion._meta.verbose_name_plural
    return render(request, "Region/region_out.html", locals())


@login_required
def region_add(request):
    form = RegionForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../../../region")
        else:
            return redirect("../../../region")
    return render(request, "Region/region_add.html", locals())


@login_required
def region_edit(request, region_id):
    region = AddressRegion.objects.get(id=region_id)
    form = RegionForm(instance=region)
    if request.method == "POST":
        form = RegionForm(request.POST, instance=region)
        if form.is_valid():
            form.save()
            return redirect("../../../region")
        else:
            return redirect("../../../region")
    return render(request, "Region/region_edit.html", locals())


@login_required
def region_delete(request, region_id):
    region = AddressRegion.objects.get(id=region_id)
    if request.method == "POST":
        print(request.POST)
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            region.is_active = False
            region.save()
            return redirect("../../../region")
        else:
            return redirect("../../../region")
    return render(request, "Region/region_delete.html", locals())


# COUNTRY
@login_required
def country_out(request):
    country_list = AddressCountry.objects.filter(is_active=True)
    country_verbose = AddressCountry._meta.verbose_name_plural
    return render(request, "Country/country_out.html", locals())


@login_required
def country_add(request):
    form = CountryForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../../../country")
        else:
            return redirect("../../../country")
    return render(request, "Country/country_add.html", locals())


@login_required
def country_edit(request, country_id):
    country = AddressCountry.objects.get(id=country_id)
    form = CountryForm(instance=country)
    if request.method == "POST":
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect("../../../country")
        else:
            return redirect("../../../country")
    return render(request, "Country/country_edit.html", locals())


@login_required
def country_delete(request, country_id):
    country = AddressCountry.objects.get(id=country_id)
    if request.method == "POST":
        print(request.POST)
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            country.is_active = False
            country.save()
            return redirect("../../../country")
        else:
            return redirect("../../../country")
    return render(request, "Country/country_delete.html", locals())


# PRODUCTS
@login_required
def product_out(request):
    product_list = Product.objects.filter(is_active=True)
    product_verbose = Product._meta.verbose_name_plural
    return render(request, "Product/product_out.html", locals())


@login_required
def product_add(request):
    form = ProductForm(request.POST or None)
    flag = False
    if request.method == "POST":
        if form.is_valid():
            if 'Add' in request.POST.keys() and request.POST['Add']:
                form.save()
                return redirect("../../../product")
            else:
                form.save()
                return redirect("../../../product/add")
        else:
            return redirect("../../../product")
    return render(request, "Product/product_add.html", locals())


@login_required
def product_edit(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("../../../product")
        else:
            return redirect("../../../product")
    return render(request, "Product/product_edit.html", locals())


@login_required
def product_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        print(request.POST)
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            product.is_active = False
            product.save()
            return redirect("../../../product")
        else:
            return redirect("../../../product")
    return render(request, "Product/product_delete.html", locals())


# PRODUCT_IN_ORDER
@login_required
def productInOrder_out(request):
    productInOrder_list = ProductInOrder.objects.filter(is_active=True)
    productInOrder_verbose = ProductInOrder._meta.verbose_name_plural
    return render(request, "ProductInOrder/productInOrder_out.html", locals())


@login_required
def productInOrder_add(request):
    form = ProductInOrderForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../../../productInOrder")
        else:
            return redirect("../../../productInOrder")
    return render(request, "ProductInOrder/productInOrder_add.html", locals())


@login_required
def productInOrder_edit(request, productInOrder_id):
    productInOrder = ProductInOrder.objects.get(id=productInOrder_id)
    form = ProductInOrderForm(instance=productInOrder)
    if request.method == "POST":
        form = ProductInOrderForm(request.POST, instance=productInOrder)
        if form.is_valid():
            form.save()
            return redirect("../../../productInOrder")
        else:
            return redirect("../../../productInOrder")
    return render(request, "ProductInOrder/productInOrder_edit.html", locals())


@login_required
def productInOrder_delete(request, productInOrder_id):
    productInOrder = ProductInOrder.objects.get(id=productInOrder_id)
    if request.method == "POST":
        print(request.POST)
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            productInOrder.is_active = False
            productInOrder.save()
            return redirect("../../../productInOrder")
        else:
            return redirect("../../../productInOrder")
    return render(request, "ProductInOrder/productInOrder_delete.html", locals())


# PAYMENT_TYPE
@login_required
def paymentType_out(request):
    paymentType_list = PaymentType.objects.filter(is_active=True)
    paymentType_verbose = PaymentType._meta.verbose_name_plural
    return render(request, "PaymentType/paymentType_out.html", locals())


@login_required
def paymentType_add(request):
    form = PaymentTypeForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../../../paymentType")
        else:
            return redirect("../../../paymentType")
    return render(request, "PaymentType/paymentType_add.html", locals())


@login_required
def paymentType_edit(request, paymentType_id):
    paymentType = PaymentType.objects.get(id=paymentType_id)
    form = PaymentTypeForm(instance=paymentType)
    if request.method == "POST":
        form = PaymentTypeForm(request.POST, instance=paymentType)
        if form.is_valid():
            form.save()
            return redirect("../../../paymentType")
        else:
            return redirect("../../../paymentType")
    return render(request, "PaymentType/paymentType_edit.html", locals())


@login_required
def paymentType_delete(request, paymentType_id):
    paymentType = PaymentType.objects.get(id=paymentType_id)
    if request.method == "POST":
        print(request.POST)
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            paymentType.is_active = False
            paymentType.save()
            return redirect("../../../paymentType")
        else:
            return redirect("../../../paymentType")
    return render(request, "PaymentType/paymentType_delete.html", locals())


# DeliveryType
@login_required
def deliveryType_out(request):
    deliveryType_list = DeliveryType.objects.filter(is_active=True)
    deliveryType_verbose = DeliveryType._meta.verbose_name_plural
    return render(request, "DeliveryType/deliveryType_out.html", locals())


@login_required
def deliveryType_add(request):
    form = DeliveryTypeForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../../../deliveryType")
        else:
            return redirect("../../../deliveryType")
    return render(request, "DeliveryType/deliveryType_add.html", locals())


@login_required
def deliveryType_edit(request, deliveryType_id):
    deliveryType = DeliveryType.objects.get(id=deliveryType_id)
    form = DeliveryTypeForm(instance=deliveryType)
    if request.method == "POST":
        form = DeliveryTypeForm(request.POST, instance=deliveryType)
        if form.is_valid():
            form.save()
            return redirect("../../../deliveryType")
        else:
            return redirect("../../../deliveryType")
    return render(request, "DeliveryType/deliveryType_edit.html", locals())


@login_required
def deliveryType_delete(request, deliveryType_id):
    deliveryType = DeliveryType.objects.get(id=deliveryType_id)
    if request.method == "POST":
        print(request.POST)
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            deliveryType.is_active = False
            deliveryType.save()
            return redirect("../../../deliveryType")
        else:
            return redirect("../../../deliveryType")
    return render(request, "DeliveryType/deliveryType_delete.html", locals())


# MANUFACTURER
@login_required
def manufacturer_out(request):
    manufacturer_list = Manufacturer.objects.filter(is_active=True)
    manufacturer_verbose = Manufacturer._meta.verbose_name_plural
    return render(request, "Manufacturer/manufacturer_out.html", locals())


@login_required
def manufacturer_add(request):
    form = ManufacturerForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../../../manufacturer")
        else:
            return redirect("../../../manufacturer")
    return render(request, "Manufacturer/manufacturer_add.html", locals())


@login_required
def manufacturer_edit(request, manufacturer_id):
    manufacturer = Manufacturer.objects.get(id=manufacturer_id)
    form = ManufacturerForm(instance=manufacturer)
    if request.method == "POST":
        form = ManufacturerForm(request.POST, instance=manufacturer)
        if form.is_valid():
            form.save()
            return redirect("../../../manufacturer")
        else:
            return redirect("../../../manufacturer")
    return render(request, "Manufacturer/manufacturer_edit.html", locals())


@login_required
def manufacturer_delete(request, manufacturer_id):
    manufacturer = Manufacturer.objects.get(id=manufacturer_id)
    if request.method == "POST":
        print(request.POST)
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            manufacturer.is_active = False
            manufacturer.save()
            return redirect("../../../manufacturer")
        else:
            return redirect("../../../manufacturer")
    return render(request, "Manufacturer/manufacturer_delete.html", locals())


# PROVIDER
@login_required
def provider_out(request):
    provider_list = Provider.objects.filter(is_active=True)
    provider_verbose = Provider._meta.verbose_name_plural
    return render(request, "Provider/provider_out.html", locals())


@login_required
def provider_add(request):
    form = ProviderForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../../../provider")
        else:
            return redirect("../../../provider")
    return render(request, "Provider/provider_add.html", locals())


@login_required
def provider_edit(request, provider_id):
    provider = Provider.objects.get(id=provider_id)
    form = ProviderForm(instance=provider)
    if request.method == "POST":
        form = ProviderForm(request.POST, instance=provider)
        if form.is_valid():
            form.save()
            return redirect("../../../provider")
        else:
            return redirect("../../../provider")
    return render(request, "Provider/provider_edit.html", locals())


@login_required
def provider_delete(request, provider_id):
    provider = Provider.objects.get(id=provider_id)
    if request.method == "POST":
        print(request.POST)
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            provider.is_active = False
            provider.save()
            return redirect("../../../provider")
        else:
            return redirect("../../../provider")
    return render(request, "Provider/provider_delete.html", locals())


# STORE
@login_required
def store_out(request):
    store_list = Store.objects.filter(is_active=True)
    store_verbose = Store._meta.verbose_name_plural
    return render(request, "Store/store_out.html", locals())


@login_required
def store_add(request):
    form = StoreForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../../../store")
        else:
            return redirect("../../../store")
    return render(request, "Store/store_add.html", locals())


@login_required
def store_edit(request, store_id):
    store = Store.objects.get(id=store_id)
    form = StoreForm(instance=store)
    if request.method == "POST":
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect("../../../store")
        else:
            return redirect("../../../store")
    return render(request, "Store/store_edit.html", locals())


@login_required
def store_delete(request, store_id):
    store = Store.objects.get(id=store_id)
    if request.method == "POST":
        print(request.POST)
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            store.is_active = False
            store.save()
            return redirect("../../../store")
        else:
            return redirect("../../../store")
    return render(request, "Store/store_delete.html", locals())


# CUSTOMER_ADDRESS
@login_required
def customerAddress_out(request):
    customerAddress_list = CustomerAddress.objects.filter(is_active=True)
    customerAddress_verbose = CustomerAddress._meta.verbose_name_plural
    return render(request, "CustomerAddress/customerAddress_out.html", locals())


@login_required
def customerAddress_add(request):
    form = CustomerAddressAddForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../../../customerAddress")
        else:
            return redirect("../../../customerAddress")
    return render(request, "CustomerAddress/customerAddress_add.html", locals())


@login_required
def customerAddress_edit(request, customerAddress_id):
    customerAddress = CustomerAddress.objects.get(id=customerAddress_id)
    form = CustomerAddressEditForm(instance=customerAddress)
    if request.method == "POST":
        form = CustomerAddressEditForm(request.POST, instance=customerAddress)
        if form.is_valid():
            form.save()
            return redirect("../../../customerAddress")
        else:
            return redirect("../../../customerAddress")
    return render(request, "CustomerAddress/customerAddress_edit.html", locals())


@login_required
def customerAddress_delete(request, customerAddress_id):
    customerAddress = CustomerAddress.objects.get(id=customerAddress_id)
    if request.method == "POST":
        print(request.POST)
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            customerAddress.is_active = False
            customerAddress.save()
            return redirect("../../../customerAddress")
        else:
            return redirect("../../../customerAddress")
    return render(request, "CustomerAddress/customerAddress_delete.html", locals())

# Create your views here.
