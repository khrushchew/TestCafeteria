from order.API.serializers.create_serializer import CreateOrderSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

class CreateOrderView(ViewSet):
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = CreateOrderSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={"detail": 'Заказ успешно создан'}, status=201)
