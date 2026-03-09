from rest_framework import serializers
from ..models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    full_address = serializers.ReadOnlyField()

    class Meta:
        model = Customer
        fields = [
            "id",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "phone",
            "street",
            "city",
            "state",
            "zip_code",
            "full_address",
            "is_active",
            "created_at",
            "updated_at",
        ]

 
