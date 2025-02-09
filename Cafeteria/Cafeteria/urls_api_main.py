from django.urls import path, include


urlpatterns = [
    path('v1/', include('order.urls_api')),
]