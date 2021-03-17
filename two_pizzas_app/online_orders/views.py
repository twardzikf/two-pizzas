from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order, Product

def order_form_view(request):
    if request.method == 'GET':
        product = Product.objects.get(pk=request.GET['product_id'])
        new_order_data = {
            'product_id': product.pk,
            'product_name': product.name,
        }
        context = {
            'form': OrderForm(new_order_data, product=product),
            'product_name': product.name,
        }
        return render(request, "order_form.html", context)

    if request.method == 'POST':
        form = OrderForm(request.POST, product=None)
        if form.is_valid(): 
            form.save()
            return redirect('order-list-view')

def order_list_view(request):
    query = ''
    if request.method == 'GET':
        query = request.GET.get('q', '')
    context = {
        'orders': Order.objects.filter(name__icontains=query) | Order.objects.filter(email__icontains=query)
    }
    return render(request, "order_list.html", context)

def product_list_view(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, "product_list.html", context)
