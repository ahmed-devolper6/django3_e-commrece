from rest_framework import serializers
from .models import Products , Brand , Catgory 

#ProudctList
class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        
#brandlist
class BrandSerializers(serializers.ModelSerializer):
    proudcts = ProductsSerializers(source='brand_product',many=True)
    class Meta:
        model = Brand
        fields = ['id','name','image','proudcts']
        

#catgorylist

class CatgorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Catgory
        fields = '__all__'
        
