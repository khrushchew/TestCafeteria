from django.db import models


class Order(models.Model):
    status_list = [('W', 'Ожидание'), ('R', 'Готово'), ('P', ' Оплачено')]

    table_number = models.ForeignKey('Table', models.CASCADE, null=False, blank=False, verbose_name='Номер стола')
    items = models.ManyToManyField('Dish')
    total_price = models.PositiveIntegerField(null=False, blank=False, default=0, editable=False, verbose_name='Общая стоимость')
    status = models.CharField(max_length=2, choices=status_list, default='W', verbose_name='Статус')

    class Meta:
        db_table = 'Order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.pk}'