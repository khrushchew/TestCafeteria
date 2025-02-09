from django import forms

from core.models.dish import Dish
from core.models.order import Order

# Форма редактирования заказа
class OrderForm(forms.ModelForm):
    # Метакласс для связи с моделью
    class Meta:
        model = Order
        fields = ('table_number', 'items', 'status')
        labels = {
            'items': 'Блюда',
            'table_number': 'Номер стола',
        }

    # Все блюда
    items = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.all(),  
        widget=forms.CheckboxSelectMultiple,  
        required=True
    )
