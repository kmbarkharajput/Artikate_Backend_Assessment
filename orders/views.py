from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .queries import get_orders
from .serializers import OrderSerializer
from .services import OrderService


class OrderListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = get_orders()
        serializer = OrderSerializer(
            queryset,
            many=True
        )

        return Response(serializer.data)


class OrderSummaryView(APIView):
    permission_classes = [AllowAny]


    def get(self, request):
        summary = OrderService.get_summary()
        return Response(summary)