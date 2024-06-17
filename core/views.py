from django.shortcuts import render

def index(request):
    context = {
        'course' : 'Programação Web com Django Framework',
    }
    return render(request, 'index.html', context)

def contact(request):
    context = {
        'number' : '12 0201023060'
    }
    return render(request, 'contact.html', context)
