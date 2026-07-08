from django.test import TestCase
from tenants.models import Tenant
from .models import Customer, Order


class OrderTests(TestCase):
    def setUp(self):
        tenant = Tenant.objects.create(
            name="Demo Tenant"
        )

        customer = Customer.objects.create(
            tenant=tenant,
            name="John Doe",
            email="john@example.com"
        )

        Order.objects.create(
            tenant=tenant,
            customer=customer,
            total=250,
            status="COMPLETED"
        )

    def test_order_created(self):
        self.assertEqual(Order.objects.count(), 1)

    def test_summary(self):
        order = Order.objects.first()
        self.assertEqual(order.status, "COMPLETED")