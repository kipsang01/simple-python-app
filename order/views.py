from rest_framework import viewsets

from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework import permissions


class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def perform_create(self, serializer):
        order = serializer.save()
        order.send_notification()
        return order
