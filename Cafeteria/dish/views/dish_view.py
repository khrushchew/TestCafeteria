from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from core.models.dish import Dish

from dish.serializers.dish_serializer import DishSerializer

class DishView(ViewSet):
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = DishSerializer(data)
        if serializer.is_valid(raise_exception=True):
            return Response(detail='Блюдо успешно добавлено!', status=201)
        else:
            return Response(serializer.error_messages)
