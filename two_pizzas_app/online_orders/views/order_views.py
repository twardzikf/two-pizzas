from django.shortcuts import render

def order_list_view(request, *args, **kwargs):
    return render(request, "order_list.html", {})

def order_form_view(request, *args, **kwargs):
    return render(request, "order_form.html", {})
