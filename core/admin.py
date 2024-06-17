from django.contrib import admin

from .models import Product, Cliente

class ProductAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')
    # mostar no admin

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

admin.site.register(Product, ProductAdmin)
admin.site.register(Cliente, ClienteAdmin)
