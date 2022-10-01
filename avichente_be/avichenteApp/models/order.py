from django.db import models

from .product import Product
from .user import User


class OrderDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, related_name='order_details_product', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField('Amount')
    price = models.PositiveIntegerField('Price')


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='order_user', on_delete=models.CASCADE)
    order_details = models.ForeignKey(OrderDetails, related_name='order_order_details', on_delete=models.CASCADE)
    price = models.PositiveIntegerField('Price')
    date = models.DateTimeField()



