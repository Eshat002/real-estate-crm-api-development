import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from customers.models import Customer
from django.urls import reverse
from unittest.mock import patch

@pytest.mark.django_db
def test_case_insensitive_filter_and_destroy():
    # Setup admin user
    admin = User.objects.create_superuser("admin", "admin@test.com", "password123")
    client = APIClient()
    client.force_authenticate(user=admin)

    # Create test customers
    c1 = Customer.objects.create(first_name="John", last_name="Doe", email="john@example.com", phone="123")
    c2 = Customer.objects.create(first_name="Jane", last_name="Smith", email="jane@example.com", phone="456")

    url = reverse("customer-list")

    # 1️⃣ Filter by first_name lowercase
    response = client.get(url, {"first_name": "john"})
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["first_name"] == "John"

    # 2️⃣ Filter by first_name uppercase
    response = client.get(url, {"first_name": "JANE"})
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["first_name"] == "Jane"

    # 3️⃣ Test perform_destroy calls deactivate_customer
    detail_url = reverse("customer-detail", args=[c1.id])
    with patch("customers.views.deactivate_customer") as mock_deactivate:
        response = client.delete(detail_url)
        mock_deactivate.assert_called_once_with(c1)
        assert response.status_code == 204  # DRF returns 204 on successful DELETE