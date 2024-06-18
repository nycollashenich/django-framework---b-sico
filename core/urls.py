from django.urls import path
# import o path, django.urls

from .views import index, contact, produto
# importei do core ".", o meu index e contact

urlpatterns = [
    path('', index, name = 'index'),
    path('contact/', contact, name = 'contact'),
    path('produto/<int:pk>', produto, name='produto'),
]
