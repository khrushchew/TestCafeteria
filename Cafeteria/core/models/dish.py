from django.db import models


class Dish(models.Model):
    name = models.TextField(null=False, blank=False, verbose_name='Название')
    price = models.PositiveIntegerField(null=False, blank=False, verbose_name='Цена')

    class Meta:
        db_table = 'Dish'
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name