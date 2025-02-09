from django.urls import path, include

from rest_framework.routers import SimpleRouter

from dish.API.views.dish_view import DishView

dish_router = SimpleRouter()
dish_router.register(r'dishes', DishView, 'dish')

urlpatterns = [
    path('', include(dish_router.urls))
]