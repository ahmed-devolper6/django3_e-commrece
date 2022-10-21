from rest_framework import serializers
from .models import Products , Brand , Catgory , Reviw 

#ProudctList
class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        
#brandlist
class BrandDetialSerializers(serializers.ModelSerializer):
    proudcts = ProductsSerializers(source='brand_product',many=True)
    class Meta:
        model = Brand
        fields = ['id','name','image','proudcts']
        
class BrandListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id','name','image']
#catgorylist

class CatgoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Catgory
        fields = '__all__'
        
class CatgoryDetilSerializers(serializers.ModelSerializer):
    proudcts = ProductsSerializers(source='Catgory_prodcut',many=True)
    class Meta:
        model = Catgory
        fields = ['id','name','image','proudcts']
        

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviw
        fields = '__all__'


class ProductsdetilSerializers(serializers.ModelSerializer):
    review = ReviewSerializers(source ='Proudct_Review',many=True)
    class Meta:
        model = Products
        fields = ['name','sku','price','image','brand','dec','subtitle','video_url' ,'review']