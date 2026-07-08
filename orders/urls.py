from django.urls import path

from .views import (
    OrderListView,
    OrderSummaryView,
)

urlpatterns = [
    path("", OrderListView.as_view(), name="orders"),
    path("summary/", OrderSummaryView.as_view(), name="order-summary"),
]