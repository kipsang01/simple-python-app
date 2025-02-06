from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from unittest.mock import patch

from .models import Customer, Order

class CustomerModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpass'
        )
        self.customer = Customer.objects.create(
            user=self.user, 
            code='TEST001', 
            phone_number='+1234567890'
        )

    def test_customer_creation(self):
        self.assertTrue(isinstance(self.customer, Customer))
        self.assertEqual(self.customer.__str__(), 'testuser')

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpass'
        )
        self.customer = Customer.objects.create(
            user=self.user, 
            code='TEST001'
        )
        self.order = Order.objects.create(
            customer=self.customer, 
            item='Test Item', 
            amount=100.00
        )

    def test_order_creation(self):
        self.assertTrue(isinstance(self.order, Order))
        self.assertEqual(self.order.__str__(), 'Test Item - testuser')

class CustomerViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpass'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_customer(self):
        data = {
            'user': self.user.id,
            'code': 'TEST002',
            'phone_number': '+254722222222'
        }
        response = self.client.post('/api/customers/', data)
        self.assertEqual(response.status_code, 201)

class OrderViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpass'
        )
        self.customer = Customer.objects.create(
            user=self.user, 
            code='TEST001',
            phone_number='+254722222222'
        )
        self.client.force_authenticate(user=self.user)

    @patch('order.models.Order.send_notification')
    def test_create_order_with_sms(self, mock_send_notification):
        data = {
            'customer': self.customer.id,
            'item': 'Test Item',
            'amount': 100.00
        }
        response = self.client.post('/api/orders/', data)

        self.assertEqual(response.status_code, 201)
        mock_send_notification.assert_called_once_with()
