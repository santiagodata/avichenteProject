from avichente_be.avichenteApp.models.order import Order, OrderDetails
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'order_details', 'price', 'date']


class OrderDetailsSerializer(serializers.ModelSerializer):

    order = OrderSerializer
    class Meta:
        model = OrderDetails
        fields = ['id', 'product', 'amount', 'price']

