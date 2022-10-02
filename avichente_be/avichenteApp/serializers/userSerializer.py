from rest_framework import serializers
from avichente_be.avichenteApp.models.user import User
from avichente_be.avichenteApp.models.order import Order
from avichente_be.avichenteApp.serializers import OrderSerializer


class UserSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'lastName', 'email', 'address', 'role']

    def create(self, validated_data):
        orderData = validated_data.pop('order')
        userInstance = User.objects.create(**validated_data)
        Order.objects.create(user=userInstance, **orderData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        order = Order.objects.get(user=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'lastName': user.lastName,
            'email': user.email,
            'address': user.address,
            'order': {
                'id': order.id,
                'user': order.user,
                'orderDetails': order.order_details,
                'price': order.price,
                'date': order.date

            }
        }
