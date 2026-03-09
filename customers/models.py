from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    street = models.CharField(max_length=255, blank= True, null=True)
    city = models.CharField(max_length=100,  blank= True, null=True)
    state = models.CharField(max_length=100,  blank= True, null=True)
    zip_code = models.CharField(max_length=20,  blank= True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_address(self):
        parts = [self.street, self.city, self.state, self.zip_code]
        return ", ".join(filter(None, parts))