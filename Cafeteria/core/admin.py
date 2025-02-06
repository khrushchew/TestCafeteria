from django.contrib import admin

from core.models.table import Table
from core.models.dish import Dish
from core.models.order import Order


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', )
    list_editable = ('price', )


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('position', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'status')
    list_editable = ('status', )
    filter_horizontal = ('items', )
    