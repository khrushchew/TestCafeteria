from django.test import TestCase
from django.urls import reverse
from core.models.order import Order
from core.models.table import Table
from order.views.home import home


class TestViews(TestCase):
    def setUp(self):
        self.table1 = Table.objects.create(position=1)
        self.table2 = Table.objects.create(position=2)
        self.table3 = Table.objects.create(position=3)

        self.order1 = Order.objects.create(table_number=self.table1, status='W', total_price=100)
        self.order2 = Order.objects.create(table_number=self.table2, status='P', total_price=200)
        self.order3 = Order.objects.create(table_number=self.table3, status='R', total_price=300)

    def test_200(self):
        self.assertEqual(self.client.get('/').status_code, 200)
        self.assertEqual(self.client.get('/admin/').status_code, 302)
        self.assertEqual(self.client.get('/waiting/').status_code, 200)
        self.assertEqual(self.client.get('/ready/').status_code, 200)
        self.assertEqual(self.client.get('/paid/').status_code, 200)
        self.assertEqual(self.client.get('/create/').status_code, 200)
        self.assertEqual(self.client.get(f'/detail/{self.order1.pk}/').status_code, 200)
