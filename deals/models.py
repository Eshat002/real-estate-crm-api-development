from django.db import models
from customers.models import Customer


class Deal(models.Model):

    class Status(models.TextChoices):
        IN_PROGRESS = "in_progress", "In Progress"
        CLOSED = "closed", "Closed"

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="deals"
    )

    property_address = models.CharField(max_length=255)

    image = models.ImageField(
        upload_to="deals/",
        blank=True,
        null=True
    )

    area = models.DecimalField(max_digits=10, decimal_places=2)

    appointment_date = models.DateTimeField()

    price = models.DecimalField(max_digits=12, decimal_places=2)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.IN_PROGRESS
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.property_address