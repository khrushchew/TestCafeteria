from django import forms
from core.models.order import Order

# Форма поиска заказов
class OrderSearchForm(forms.Form):
    # Номер стола
    table_number = forms.ChoiceField(
        choices= [(0, 'Все')] + [(order.table_number, order.table_number) for order in Order.objects.all()],
        required=False,
        label='Номер стола',
        initial=0
    )

    # Статус
    status = forms.ChoiceField(
        choices=[('A', 'Все'), ('W', 'Ожидание'), ('R', 'Готово'), ('P', ' Оплачено')],
        required=False,
        label='Статус',
        initial='A'
    )
