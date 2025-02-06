from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order.views.list import ListOrderView

router = DefaultRouter()
router.register(r'orders', ListOrderView, 'order')

urlpatterns = [
    path('v1/', include(router.urls))
]