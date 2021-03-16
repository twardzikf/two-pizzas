"""two_pizzas_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from online_orders.views.order_views import order_form_view, order_list_view
from online_orders.views.product_views import product_list_view

urlpatterns = [
    path('', product_list_view, name='product_list'),
    path('orders/', order_list_view, name='order_list'),
    path('make_order/', order_form_view, name='order_form'),
    path('admin/', admin.site.urls),
]
