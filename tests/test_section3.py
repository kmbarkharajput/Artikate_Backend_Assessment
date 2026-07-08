from django.test import TestCase
from tenants.context import set_current_tenant
from tenants.models import Tenant
from orders.models import Customer, Order


class TenantIsolationTests(TestCase):
    def setUp(self):
        self.tenant1 = Tenant.objects.create(
            name="Tenant A",
            subdomain="a"
        )

        self.tenant2 = Tenant.objects.create(
            name="Tenant B",
            subdomain="b"
        )

        customer1 = Customer.objects.create(
            tenant=self.tenant1,
            name="Alice",
            email="alice@test.com"
        )

        customer2 = Customer.objects.create(
            tenant=self.tenant2,
            name="Bob",
            email="bob@test.com"
        )

        Order.objects.create(
            tenant=self.tenant1,
            customer=customer1,
            total=100,
            status="COMPLETED"
        )

        Order.objects.create(
            tenant=self.tenant2,
            customer=customer2,
            total=200,
            status="COMPLETED"
        )

    def test_tenant_context(self):
        set_current_tenant(self.tenant1)
        orders = Order.objects.filter(tenant=self.tenant1)
        self.assertEqual(orders.count(), 1)

    def test_two_tenants_exist(self):
        self.assertEqual(Tenant.objects.count(), 2)