from django.contrib import admin
from .models.product import Product
from .models.order import Order

admin.site.register(Order)
admin.site.register(Product)