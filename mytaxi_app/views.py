from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView
)

from mytaxi_app.models import Order
from mytaxi_app.serializer import OrderSerializer, OrderUpdateSerializer


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'datetime': ['gte', 'lte']
    }


class OrderCreateAPIView(CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response({
                "message": "Successfully created",
                "order_id": instance.id,
                "http_status": status.HTTP_201_CREATED
            })
        return Response({
            "message": serializer.errors,
            "http_status": status.HTTP_400_BAD_REQUEST
        })


class OrderUpdateAPIView(UpdateAPIView):
    queryset = Order.objects.all()
    lookup_field = 'pk'
    serializer_class = OrderUpdateSerializer

    def put(self, request, *args, **kwargs):

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Order updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})
