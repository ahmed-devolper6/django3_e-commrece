from django_filters import rest_framework
from .models import Products
class CustomFilter(rest_framework.FilterSet):
    class Meta:
        model = Products 
        fields = {
            'name': ['icontains'],
            'price': ['lte','gte'],
        }