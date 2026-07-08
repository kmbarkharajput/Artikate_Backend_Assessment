from rest_framework.response import Response
from rest_framework.views import APIView


class CurrentTenantView(APIView):
    def get(self, request):
        if hasattr(request, "tenant"):
            return Response({
                "id": request.tenant.id,
                "name": request.tenant.name,
                "subdomain": request.tenant.subdomain,
            })

        return Response({
            "message": "No tenant selected."
        })