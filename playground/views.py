from unicodedata import name
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import Product

# Create your views here.
def say_hello(request):
  
    # products = Product.objects.filter(unit_price__gt = 20)
    queryset = Product.objects.filter(unit_price__range =(20, 30))
    print('product ', products)

    

    return render(request, 'hello.html',{'name':'simon J','products':list(queryset)})
