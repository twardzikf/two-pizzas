from django.http import HttpResponse
from django.shortcuts import render

def product_list_view(request, *args, **kwargs):
    return render(request, "product_list.html", {})