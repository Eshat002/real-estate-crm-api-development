from .models import Customer

def deactivate_customer(customer: Customer):
    customer.is_active = False
    customer.save()
