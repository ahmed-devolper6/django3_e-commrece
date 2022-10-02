from .serializers import ProductsSerializers
from .models import Products
from rest_framework.views import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def proudct_list_api(request):
    objects = Products.objects.all()
    data = ProductsSerializers(objects , many = True).data
    return Response({'status':200 , 'products':data})


@api_view(['GET'])
def proudct_detail_api(request , id):
    objects = Products.objects.get(id = id)
    data = ProductsSerializers(objects).data
    return Response({'status':200 , 'product':data})

class Proudctdetil_api(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
 
class ProudctList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers


