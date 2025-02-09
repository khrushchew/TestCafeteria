from django import forms
from core.models.order import Order
from core.models.dish import Dish
from django.forms import ValidationError

# Форма добавления заказа
class AddOrderForm(forms.ModelForm):
    # Метакласс для связи с моделью
    class Meta:
        model = Order
        fields = ('table_number', 'items')
        labels = {
            'items': 'Блюда',
            'table_number': 'Номер стола',
        }

    # Все блюда чекбоксами
    items = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    # Доп проверка формы на корректность
    def clean(self):
        cleaned_data = super().clean()
        table_number = cleaned_data.get('table_number')
        
        if table_number and Order.objects.filter(table_number=table_number, status__in=['W', 'R']).exists():
            raise ValidationError('На этом столе уже есть заказ в статусе "Ожидание" или "Готово".')

        return cleaned_data
