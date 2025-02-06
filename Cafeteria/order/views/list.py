from order.serializers.list_order import ListOrderSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from core.models.order import Order

class ListOrderView(ViewSet):
    def list(self, request, *args, **kwargs):
        obj = Order.objects.all()
        serializer = ListOrderSerializer(obj, many=True)
        return Response(data=serializer, status=200)
