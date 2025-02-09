from django.shortcuts import render, redirect
from order.forms.create_order import AddOrderForm 

# Создание заказа
def create_order(request):
    if request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            selected_dishes = form.cleaned_data['items']
            order.items.set(selected_dishes)
            order.total_price = sum(dish.price for dish in selected_dishes)
            order.save()
            return redirect('/waiting/')
    else:
        form = AddOrderForm()
    return render(request, 'crud/create_page.html', {'form': form})
