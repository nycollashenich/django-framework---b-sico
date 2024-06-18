from django.shortcuts import render
from core.models import Product

def index(request):
    products = Product.objects.all()
    context = {
        'course' : 'Programação Web com Django Framework',
        'products' : products,
    }
    return render(request, 'index.html', context)

def contact(request):
    context = {
        'number' : '12 0201023060'
    }
    return render(request, 'contact.html', context)

def produto(request, pk):
    prod = Product.objects.get(id=pk)
    
    context = {
        'produto': prod,
    }
    
    return render(request, 'produto.html', context)
