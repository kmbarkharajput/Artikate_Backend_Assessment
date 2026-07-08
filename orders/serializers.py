from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.CharField(source="customer.name")
    class Meta:
        model = Order
        fields = [
            "id",
            "customer",
            "status",
            "total",
            "created_at",
        ]