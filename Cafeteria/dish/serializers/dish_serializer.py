from rest_framework import serializers

from core.models.dish import Dish


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', 'price')
