from django.shortcuts import render
from core.models.order import Order


def waiting_view(request):
    orders = Order.objects.filter(status='W').order_by('table_number')
    return render(request, 'stages/waiting.html', context={'orders': orders})
