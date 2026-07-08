from .models import Order


def get_orders():
    return Order.objects.select_related(
    "customer",
    "tenant",
)