from rest_framework import serializers

from avichente_be.avichenteApp.models.product import Product
from avichente_be.avichenteApp.models.order import Order, OrderDetails
from avichente_be.avichenteApp.serializers import OrderDetailsSerializer


class ProductSerializer(serializers.ModelSerializer):
    orderDetails = OrderDetailsSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

    def create(self, validated_data):
        orderDetailsData = validated_data.pop('orderDetails')
        productInstance = Product.objects.create(**validated_data)
        OrderDetails.objects.create(product=productInstance, **orderDetailsData)
        return productInstance

    def to_representation(self, obj):
        product = Product.objects.get(id=obj.id)
        orderDetails = Order.objects.get(product=obj.id)
        return {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'orderDetails': {
                'id': orderDetails.id,
                'product': orderDetails.product,
                'amount': orderDetails.amount,
                'price': orderDetails.price

            }
        }


