from order.API.views import list_view, retrieve_view, create_view
from rest_framework.viewsets import ViewSet

class OrderView(list_view.ListOrderView, retrieve_view.RetrieveOrderView, create_view.CreateOrderView):
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
