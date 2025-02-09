from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from core.models.dish import Dish

from dish.API.serializers.dish_serializer import TableSerializer

class DishView(ViewSet):
    def get_dish(self):
        try:
            dish = Dish.objects.get(pk=self.kwargs.get('pk')) 
            return dish
        except:
            raise NotFound(detail='Блюдо не найдено!')

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = TableSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={"detail": 'Блюдо успешно добавлено!'}, status=201)

    def list(self, request, *args, **kwargs):
        dishes = Dish.objects.all()
        serializer = TableSerializer(dishes, many=True)
        try:
            return Response(serializer.data, status=200)
        except:
            return Response(data={'detail': 'Ошибка сервера'}, status=500)
    
    def retrieve(self, request, *args, **kwargs):
        dish = self.get_dish()
        serializer = TableSerializer(dish)
        return Response(serializer.data, status=200)
    
    def partial_update(self, request, *args, **kwargs):
        data = request.data
        dish = Dish.objects.get(pk=kwargs.get('pk'))
        serializer = TableSerializer(dish, data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'detail': 'Данные обновлены'}, status=200)

    def update(self, request, *args, **kwargs):
        data = request.data

        dish = Dish.objects.get(pk=kwargs.get('pk'))

        serializer = TableSerializer(dish, data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'detail': 'Данные обновлены'}, status=200)
    
    def destroy(self, request, *args, **kwargs):
        dish = self.get_dish()
        dish.delete()
        return Response({'detail': 'Данные удалены'}, status=200)
