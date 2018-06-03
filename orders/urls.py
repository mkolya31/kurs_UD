from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    # CUSTOMER
    url(r'^customer$', views.customer_out, name='customer_out'),
    url(r'^customer/add$', views.customer_add, name='customer_add'),
    url(r'^customer/view/(?P<customer_id>[\w-]+)$', views.customer_view, name='customer_view'),
    url(r'^customer/edit/(?P<customer_id>[\w-]+)$', views.customer_edit, name='customer_edit'),
    url(r'^customer/delete/(?P<customer_id>[\w-]+)$', views.customer_delete, name='customer_delete'),
    # ADDRESS
    url(r'^address$', views.address_out, name='address_out'),
    url(r'^address/add$', views.address_add, name='address_add'),
    url(r'^address/edit/(?P<address_id>[\w-]+)$', views.address_edit, name='address_edit'),
    url(r'^address/delete/(?P<address_id>[\w-]+)$', views.address_delete, name='address_delete'),
    # BANK
    url(r'^bank$', views.bank_out, name='bank_out'),
    url(r'^bank/add$', views.bank_add, name='bank_add'),
    url(r'^bank/edit/(?P<bank_id>[\w-]+)$', views.bank_edit, name='bank_edit'),
    url(r'^bank/delete/(?P<bank_id>[\w-]+)$', views.bank_delete, name='bank_delete'),
    # DELIVERY
    url(r'^delivery$', views.delivery_out, name='delivery_out'),
    url(r'^delivery/add$', views.delivery_add, name='delivery_add'),
    url(r'^delivery/edit/(?P<delivery_id>[\w-]+)$', views.delivery_edit, name='delivery_edit'),
    url(r'^delivery/delete/(?P<delivery_id>[\w-]+)$', views.delivery_delete, name='delivery_delete'),
    # ORDERS
    url(r'^order$', views.order_out, name='order_out'),
    url(r'^order/add$', views.order_add, name='order_add'),
    url(r'^order/edit/(?P<order_id>[\w-]+)$', views.order_edit, name='order_edit'),
    url(r'^order/delete/(?P<order_id>[\w-]+)$', views.order_delete, name='order_delete'),
    # CATEGORY
    url(r'^category$', views.category_out, name='category_out'),
    url(r'^category/add$', views.category_add, name='category_add'),
    url(r'^category/edit/(?P<category_id>[\w-]+)$', views.category_edit, name='category_edit'),
    url(r'^category/delete/(?P<category_id>[\w-]+)$', views.category_delete, name='category_delete'),
    # CITY
    url(r'^city$', views.city_out, name='city_out'),
    url(r'^city/add$', views.city_add, name='city_add'),
    url(r'^city/edit/(?P<city_id>[\w-]+)$', views.city_edit, name='city_edit'),
    url(r'^city/delete/(?P<city_id>[\w-]+)$', views.city_delete, name='city_delete'),
    # ORGANIZATION
    url(r'^organization$', views.organization_out, name='organization_out'),
    url(r'^organization/add$', views.organization_add, name='organization_add'),
    url(r'^organization/edit/(?P<organization_id>[\w-]+)$', views.organization_edit, name='organization_edit'),
    url(r'^organization/delete/(?P<organization_id>[\w-]+)$', views.organization_delete, name='organization_delete'),
    # PAYMENT
    url(r'^payment$', views.payment_out, name='payment_out'),
    url(r'^payment/add$', views.payment_add, name='payment_add'),
    url(r'^payment/edit/(?P<payment_id>[\w-]+)$', views.payment_edit, name='payment_edit'),
    url(r'^payment/delete/(?P<payment_id>[\w-]+)$', views.payment_delete, name='payment_delete'),
    # REGION
    url(r'^region$', views.region_out, name='region_out'),
    url(r'^region/add$', views.region_add, name='region_add'),
    url(r'^region/edit/(?P<region_id>[\w-]+)$', views.region_edit, name='region_edit'),
    url(r'^region/delete/(?P<region_id>[\w-]+)$', views.region_delete, name='region_delete'),
    # COUNTRY
    url(r'^country$', views.country_out, name='country_out'),
    url(r'^country/add$', views.country_add, name='country_add'),
    url(r'^country/edit/(?P<country_id>[\w-]+)$', views.country_edit, name='country_edit'),
    url(r'^country/delete/(?P<country_id>[\w-]+)$', views.country_delete, name='country_delete'),
    # PRODUCT
    url(r'^product$', views.product_out, name='product_out'),
    url(r'^product/add$', views.product_add, name='product_add'),
    url(r'^product/edit/(?P<product_id>[\w-]+)$', views.product_edit, name='product_edit'),
    url(r'^product/delete/(?P<product_id>[\w-]+)$', views.product_delete, name='product_delete'),
    # PRODUCT_IN_ORDER
    url(r'^productInOrder$', views.productInOrder_out, name='productInOrder_out'),
    url(r'^productInOrder/add$', views.productInOrder_add, name='productInOrder_add'),
    url(r'^productInOrder/edit/(?P<productInOrder_id>[\w-]+)$', views.productInOrder_edit, name='productInOrder_edit'),
    url(r'^productInOrder/delete/(?P<productInOrder_id>[\w-]+)$', views.productInOrder_delete, name='productInOrder_delete'),
    # PAYMENT_TYPE
    url(r'^paymentType$', views.paymentType_out, name='paymentType_out'),
    url(r'^paymentType/add$', views.paymentType_add, name='paymentType_add'),
    url(r'^paymentType/edit/(?P<paymentType_id>[\w-]+)$', views.paymentType_edit, name='paymentType_edit'),
    url(r'^paymentType/delete/(?P<paymentType_id>[\w-]+)$', views.paymentType_delete, name='paymentType_delete'),
    # DELIVERY_TYPE
    url(r'^deliveryType$', views.deliveryType_out, name='deliveryType_out'),
    url(r'^deliveryType/add$', views.deliveryType_add, name='deliveryType_add'),
    url(r'^deliveryType/edit/(?P<deliveryType_id>[\w-]+)$', views.deliveryType_edit, name='deliveryType_edit'),
    url(r'^deliveryType/delete/(?P<deliveryType_id>[\w-]+)$', views.deliveryType_delete, name='deliveryType_delete'),
    # MANUFACTURER
    url(r'^manufacturer$', views.manufacturer_out, name='manufacturer_out'),
    url(r'^manufacturer/add$', views.manufacturer_add, name='manufacturer_add'),
    url(r'^manufacturer/edit/(?P<manufacturer_id>[\w-]+)$', views.manufacturer_edit, name='manufacturer_edit'),
    url(r'^manufacturer/delete/(?P<manufacturer_id>[\w-]+)$', views.manufacturer_delete, name='manufacturer_delete'),
    # PROVIDER
    url(r'^provider$', views.provider_out, name='provider_out'),
    url(r'^provider/add$', views.provider_add, name='provider_add'),
    url(r'^provider/edit/(?P<provider_id>[\w-]+)$', views.provider_edit, name='provider_edit'),
    url(r'^provider/delete/(?P<provider_id>[\w-]+)$', views.provider_delete, name='provider_delete'),
    # STORE
    url(r'^store$', views.store_out, name='store_out'),
    url(r'^store/add$', views.store_add, name='store_add'),
    url(r'^store/edit/(?P<store_id>[\w-]+)$', views.store_edit, name='store_edit'),
    url(r'^store/delete/(?P<store_id>[\w-]+)$', views.store_delete, name='store_delete')
]
