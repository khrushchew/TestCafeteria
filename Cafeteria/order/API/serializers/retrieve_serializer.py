from core.models.order import Order
from rest_framework import serializers


class RetrieveOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('table_number', 'items', 'total_price', 'status')
        depth = 1
