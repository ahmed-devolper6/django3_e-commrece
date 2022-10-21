from .serializers import ProductsSerializers , BrandDetialSerializers,ProductsdetilSerializers , BrandListSerializers , CatgoryListSerializers , CatgoryDetilSerializers
from .models import Products , Brand , Catgory , Reviw
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics



class ProudctDetil_Api(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsdetilSerializers
    permission_classes = [IsAuthenticated]
class ProudctList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    permission_classes = [IsAuthenticated]

class BrandList_api(generics.ListCreateAPIView):
    queryset =  Brand.objects.all()
    serializer_class = BrandListSerializers

class BrandDetil_Api(generics.RetrieveAPIView):
    queryset =  Brand.objects.all()
    serializer_class = BrandDetialSerializers

class CatgoryList_api(generics.ListCreateAPIView):
    queryset =  Catgory.objects.all()
    serializer_class = CatgoryListSerializers

class CatgoryDetil_Api(generics.RetrieveAPIView):
    queryset =  Catgory.objects.all()
    serializer_class = CatgoryDetilSerializers