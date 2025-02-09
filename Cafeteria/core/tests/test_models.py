from django.db import DataError
from django.forms import ValidationError

from django.test import TestCase

from core.models.table import Table
from core.models.dish import Dish
from core.models.order import Order


class TestTable(TestCase):
    def setUp(self):
        self.table = Table(position=1)
    
    def test_create_table(self):
        self.assertIsInstance(self.table, Table)

    def test_save_table(self):
        table = Table()
        table.position = 1
        table.save()

        self.assertEqual(Table.objects.all().count(), 1)
        self.assertEqual(self.get_postition(), 1)
    
    def get_postition(self):
        return self.table.position

    def test_edit_table(self):
        self.table.position = 7
        self.assertEqual(self.get_postition(), 7)


class TestDish(TestCase):
    def setUp(self):
        self.dish = Dish()
    
    def test_set_name(self):
        self.dish.name = 'TestData'
        self.assertTrue(self.dish.name)
        self.assertEqual(self.dish.name, 'TestData')
    
    def test_negative_set_price(self):
        self.dish.price = None
        with self.assertRaises(ValidationError):
            self.dish.full_clean()


class TestOrder(TestCase):
    def setUp(self):
        self.table = Table.objects.create(position=1)
        self.dish1 = Dish.objects.create(name='Dish 1', price=100)
        self.dish2 = Dish.objects.create(name='Dish 2', price=200)

        self.order = Order.objects.create(table_number=self.table, total_price=300, status='W')
        self.order.items.add(self.dish1, self.dish2)

    def test_order_creation(self):
        self.assertEqual(self.order.table_number.position, 1)
        self.assertEqual(self.order.total_price, 300)
        self.assertEqual(self.order.status, 'W')
        self.assertEqual(self.order.items.count(), 2)

    def test_order_status_choices(self):
        valid_statuses = ['W', 'R', 'P']
        for status in valid_statuses:
            order = Order.objects.create(table_number=self.table, total_price=100, status=status)
            self.assertEqual(order.status, status)

    def test_order_str(self):
        self.assertEqual(str(self.order), str(self.order.pk))

    def test_order_default_status(self):
        order = Order.objects.create(table_number=self.table, total_price=100)
        self.assertEqual(order.status, 'W')

    def test_status_choices(self):
        with self.assertRaises(DataError):
            Order.objects.create(table_number=self.table, total_price=100, status='345345345')
