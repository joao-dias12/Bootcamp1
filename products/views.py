from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

def home_view(request, *args, **kwargs):

    return HttpResponse("<h1> Hello world</h1>")
def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    return HttpResponse(f"Product id {obj.id}")