from order.API.serializers.retrieve_serializer import RetrieveOrderSerializer

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from rest_framework.exceptions import NotFound

from core.models.order import Order

class RetrieveOrderView(ViewSet):
    def retrieve(self, request, *args, **kwargs):
        try:
            obj = Order.objects.get(pk=int(kwargs.get('pk')))
        except:
            raise NotFound(detail='Такого заказа не существует')
        serializer = RetrieveOrderSerializer(obj)
        return Response(data=serializer.data, status=200)
