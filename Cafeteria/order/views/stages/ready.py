from django.shortcuts import render
from core.models.order import Order


def ready_view(request):
    orders = Order.objects.filter(status='R').order_by('table_number')
    return render(request, 'stages/ready.html', context={'orders': orders})
