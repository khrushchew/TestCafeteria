from order.API.views import list_view, retrieve_view
from rest_framework.viewsets import ViewSet

class OrderView(list_view.ListOrderView, retrieve_view.RetrieveOrderView, ViewSet):
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
