from django.db import models


class Table(models.Model):
    position = models.PositiveIntegerField(null=False, blank=False, verbose_name='Номер стола')

    class Meta:
        db_table = 'Table'
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'

    def __str__(self):
        return f'{self.position}'
