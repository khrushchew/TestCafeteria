from order.serializers.create_oder import CreateOrderSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

class CreateOrderView(ViewSet):
    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(request)