from django.test import TestCase
from .models import Tenant


class TenantTests(TestCase):
    def test_create_tenant(self):
        tenant = Tenant.objects.create(
            name="Acme Inc",
            subdomain="acme",
        )

        self.assertEqual(tenant.name, "Acme Inc")
        self.assertEqual(tenant.subdomain, "acme")