from django.db import models

# python manage.py makemigrations
# python manage.py migrate

class Product(models.Model):
    nome = models.CharField('Nome', max_length= 100)
    preco = models.DecimalField('Preço', decimal_places= 2, max_digits=8)
    estoque = models.IntegerField("Quantidade em Estoque")

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length= 100)
    sobrenome = models.CharField('Sobrenome', max_length= 100)
    email = models.EmailField(max_length=254)