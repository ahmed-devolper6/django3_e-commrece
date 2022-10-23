from .models import Products
from rest_framework.pagination import PageNumberPagination


class CoustomPagtions(PageNumberPagination):
    page_size = 50