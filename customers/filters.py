 
from django_filters.rest_framework import FilterSet, CharFilter
from customers.models import Customer

class CustomerFilter(FilterSet):
    first_name = CharFilter(field_name="first_name", lookup_expr="iexact")
    last_name = CharFilter(field_name="last_name", lookup_expr="iexact")
    email = CharFilter(field_name="email", lookup_expr="iexact")

    class Meta:
        model = Customer
        fields = ["is_active", "first_name", "last_name", "email"]