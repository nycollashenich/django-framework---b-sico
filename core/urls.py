from django.urls import path
# import o path, django.urls

from .views import index, contact
# importei do core ".", o meu index e contact

urlpatterns = [
    path('', index),
    path('contact/', contact),
]
