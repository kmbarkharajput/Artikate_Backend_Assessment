from django.db import models
from .context import get_current_tenant


class TenantManager(models.Manager):
    def get_queryset(self):
        tenant = get_current_tenant()
        queryset = super().get_queryset()

        if tenant is None:
            return queryset.none()

        return queryset.filter(tenant=tenant)