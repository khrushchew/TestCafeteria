from core.models.order import Order
from rest_framework import serializers


class ListOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('pk', 'table_number', 'items', 'total_price', 'status')
        depth = 1
