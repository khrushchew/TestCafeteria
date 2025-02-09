from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import UpdateView
from core.models.order import Order
from order.forms.detail import OrderForm

# Заказ детально
class OrderDetailView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'crud/order_detail.html'
    context_object_name = 'order'

    def get_success_url(self):
        return '/'
    
    def post(self, request, *args, **kwargs):
        if 'delete' in request.POST:
            return self.delete_order(request, *args, **kwargs)
        else:
            return super().post(request, *args, **kwargs)

    # Пересчёт суммы
    def form_valid(self, form):
        order = form.save(commit=False)
        selected_dishes = form.cleaned_data['items']
        order.total_price = sum(dish.price for dish in selected_dishes)
        order.save()
        order.items.set(selected_dishes)
        return super().form_valid(form)

    # Колхозненькое удаление в update)
    def delete_order(self, request, *args, **kwargs):
        order = self.get_object()
        order.delete()
        messages.success(request, "Заказ успешно удален.")
        return redirect('/')
