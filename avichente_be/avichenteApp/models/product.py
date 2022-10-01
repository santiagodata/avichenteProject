from django.db import models


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('Name', max_length=15, unique=True)
    description = models.CharField('Description', max_length=256)
    price = models.PositiveIntegerField('Price')
