from django.urls import path, include

from rest_framework.routers import SimpleRouter

from order.API.views.view import OrderView

order_router = SimpleRouter()
order_router.register(r'orders', OrderView, 'order')

urlpatterns = [
    path('', include(order_router.urls))
]