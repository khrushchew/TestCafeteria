from django.shortcuts import render
from core.models.order import Order

from django.db.models import Sum

def paid_view(request):
    orders = Order.objects.filter(status='P').order_by('table_number')
    total = orders.aggregate(total_sum=Sum('total_price'))['total_sum']
    total_tables = orders.values('table_number').annotate(total_sum=Sum('total_price')).order_by('table_number')
    return render(request, 'stages/paid.html', context={'orders': orders, 'total': total, 'total_tables': total_tables})
