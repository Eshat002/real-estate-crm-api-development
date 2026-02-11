# pagination.py
from rest_framework.pagination import CursorPagination

class CustomerCursorPagination(CursorPagination):
    page_size = 2
    ordering = "-created_at"   # MUST match your view ordering
