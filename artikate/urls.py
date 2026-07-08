from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/orders/", include("orders.urls")),
    path("api/jobs/", include("jobs.urls")),
    path("api/tenants/", include("tenants.urls")),
    path('silk/', include('silk.urls', namespace='silk')),
]