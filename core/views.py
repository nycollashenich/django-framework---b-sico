from django.shortcuts import render
from django.shortcuts import get_object_or_404
from core.models import Product
from django.http import HttpResponse
from django.template import loader

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
    # prod = Product.objects.get(id=pk)
    prod = get_object_or_404(Product, id=pk)
    context = {
        'produto': prod,
    }
    
    return render(request, 'produto.html', context)

# esse está no urls
def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type= 'text/html; charset=utf8', status= 404)

def error500(request,ex):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type= 'text/html; charset=utf8', status= 500)