from django.urls import path, include

from order.views.home import home

from order.views.stages.waiting import waiting_view
from order.views.stages.ready import ready_view
from order.views.stages.paid import paid_view

from order.views.crud.create import create_order
from order.views.crud.detail import OrderDetailView

urlpatterns = [
    path('', home, name='home'),

    path('waiting/', waiting_view, name='waiting'),
    path('ready/', ready_view, name='ready'),
    path('paid/', paid_view, name='paid'),

    path('create/', create_order, name='create'),

    path('detail/<int:pk>/', OrderDetailView.as_view(), name='detail'),
]