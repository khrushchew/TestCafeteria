from rest_framework import serializers

from core.models.dish import Dish


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('pk', 'name', 'price')
