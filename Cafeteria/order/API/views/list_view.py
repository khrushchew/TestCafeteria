from order.API.serializers.list_serializer import ListOrderSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from core.models.order import Order

class ListOrderView(ViewSet):
    def list(self, request, *args, **kwargs):
        obj = Order.objects.all()
        serializer = ListOrderSerializer(obj, many=True)
        return Response(data=serializer.data, status=200)
