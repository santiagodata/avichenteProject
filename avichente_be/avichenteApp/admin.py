from django.contrib import admin

from .models.order import Order, OrderDetails
from .models.product import Product
from .models.user import User

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderDetails)
