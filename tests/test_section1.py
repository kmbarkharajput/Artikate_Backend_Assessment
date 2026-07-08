from django.test import TestCase
from django.urls import reverse
from tenants.models import Tenant
from orders.models import Customer, Order


class OrderSummaryTests(TestCase):
    def setUp(self):
        self.tenant = Tenant.objects.create(
            name="Acme",
            subdomain="acme"
        )

        self.customer = Customer.objects.create(
            tenant=self.tenant,
            name="John Doe",
            email="john@example.com"
        )

        Order.objects.create(
            tenant=self.tenant,
            customer=self.customer,
            total=150,
            status="COMPLETED"
        )

        Order.objects.create(
            tenant=self.tenant,
            customer=self.customer,
            total=250,
            status="PENDING"
        )

    def test_summary_endpoint(self):
        response = self.client.get("/api/orders/summary/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["total_orders"], 2)
        self.assertEqual(data["completed_orders"], 1)