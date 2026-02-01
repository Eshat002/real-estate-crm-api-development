from django.shortcuts import render
from .services import deactivate_customer
# Create your views here.
def home(request):
    print(deactivate_customer)