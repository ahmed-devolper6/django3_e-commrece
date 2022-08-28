
from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Products , ProductsImages
class ProudctView(ListView):
    model = Products

class ProudctDetail(DetailView):
    model = Products

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        myproducts = self.get_object()
        context['images'] = ProductsImages.objects.filter(products=myproducts)
        context['realated'] = Products.objects.filter(catgory = myproducts.catgory)
        return context
