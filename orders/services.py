from django.db.models import Count, Sum
from .models import Order


class OrderService:
    @staticmethod
    def get_summary():
        queryset = Order.objects.all()
        return {
            "total_orders": queryset.count(),
            "completed_orders": queryset.filter(
                status="COMPLETED"
            ).count(),
            "total_revenue": queryset.aggregate(
                Sum("total")
            )["total__sum"] or 0,
        }