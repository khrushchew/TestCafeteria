from django.urls import path, include

from rest_framework.routers import SimpleRouter

from table.API.views.table_view import TableView

table_router = SimpleRouter()
table_router.register(r'tables', TableView, 'table')

urlpatterns = [
    path('', include(table_router.urls))
]