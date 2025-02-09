from django.shortcuts import render
from order.forms.search import OrderSearchForm
from core.models.order import Order

# Дом с поиском
def home(request):
    orders = Order.objects.all()
    form = OrderSearchForm(request.GET)

    if form.is_valid():
        table_number = form.cleaned_data.get('table_number')
        status = form.cleaned_data.get('status')

        if table_number == '0':
            orders = orders
        elif table_number:
            orders = orders.filter(table_number=table_number)
        if status == 'A':
            orders = orders.filter(status__in=['W', 'R', 'P'])
        if status == 'W' or status == 'R' or status == 'P':
            orders = orders.filter(status=status)

    return render(request, 'base.html', {'search_form': form, 'orders': orders})
