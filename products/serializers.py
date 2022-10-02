from rest_framework import serializers
from .models import Products

def price_with_tax(request):
    price = Products.price
    return int(price)*1.1
class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        