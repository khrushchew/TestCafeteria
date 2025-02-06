from core.models.order import Order
from rest_framework import serializers


class CreateOrderSerializer(serializers.Serializer):
    class Meta:
        db_model = Order
        fields = ('table_number', 'items', 'total_price', 'status')
