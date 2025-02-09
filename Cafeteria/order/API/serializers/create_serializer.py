from core.models.order import Order
from rest_framework import serializers


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('table_number', 'items', 'status')

    