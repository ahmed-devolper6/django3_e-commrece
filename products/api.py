from .serializers import ProductsSerializers , BrandSerializers , CatgorySerializers
from .models import Products , Brand , Catgory
from rest_framework.views import Response
from rest_framework.decorators import api_view
from rest_framework import generics



class ProudctDetil_Api(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
 
class ProudctList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers


class BrandList_api(generics.ListCreateAPIView):
    queryset =  Brand.objects.all()
    serializer_class = BrandSerializers

class BrandDetil_Api(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Brand.objects.all()
    serializer_class = BrandSerializers

class CatgoryList_api(generics.ListCreateAPIView):
    queryset =  Catgory.objects.all()
    serializer_class = CatgorySerializers

class CatgoryDetil_Api(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Catgory.objects.all()
    serializer_class = CatgorySerializers
