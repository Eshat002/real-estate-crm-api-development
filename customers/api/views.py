from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from customers.models import Customer
from .serializers import CustomerSerializer
from customers.services import deactivate_customer
from .pagination import CustomerCursorPagination

class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    pagination_class = CustomerCursorPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["first_name", "last_name", "email", "phone"]
    ordering_fields = ["created_at", "first_name"]
    ordering = ["created_at"]
    filterset_fields = ["is_active", "first_name", "last_name", "email"]

    def perform_destroy(self, instance):
        deactivate_customer(instance)   