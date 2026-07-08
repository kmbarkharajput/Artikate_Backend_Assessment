from django.http import HttpResponseBadRequest
from .context import set_current_tenant
from .models import Tenant


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant_id = request.headers.get("X-Tenant-ID")

        if tenant_id:
            try:
                tenant = Tenant.objects.get(id=tenant_id)
                set_current_tenant(tenant)
                request.tenant = tenant
            except Tenant.DoesNotExist:
                return HttpResponseBadRequest("Invalid tenant")

        response = self.get_response(request)

        return response