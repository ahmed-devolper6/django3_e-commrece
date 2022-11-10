from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Products , ProductsImages , Brand , Catgory , Reviw
from django.db.models import Count , Q , F , Value
from django.db.models.aggregates import Min , Max , Sum , Avg
from django.db.models.functions import Concat
from .froms import ProudctReviewFrom
def tester(request):
    obj = Products.objects.all()
    #obj = Products.objects.filter(price__range = (0,100))
    #obj = Products.objects.filter(price__range = (0,100)).order_by('-name')
    #obj = Products.objects.select_related('brand').all().order_by('-price')
    #obj =   Products.objects.select_related('brand').filter()
    #obj = Products.objects.filter(Q(name__endswith = 'S') & Q(price__lt = 80))
    #obj = Products.objects.filter(flag__isnull = True)
    #obj = Products.objects.filter(Q(qounitiy__lt = 50) & Q(price__lt = 70))
    #obj = Products.objects.filter(qounitiy = F('price'))
    #obj = Products.objects.filter(qounitiy = F('catgory__id'))
    #obj = Products.objects.values('name' , 'catgory' , 'catgory__id' , 'price')
    #obj = Products.objects.only('name' , 'catgory')
    #obj = Products.objects.annotate(is_new = Value(True))
    #obj = Products.objects.annotate(
    #    full_name = Concat('name' , Value(' ') , 'flags' )
    #)
    return render(request , 'products/test.html' , {'test':obj})
class ProudctView(ListView):
    model = Products
    paginate_by = 100
class ProudctDetail(DetailView):
    model = Products

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        myproducts = self.get_object()
        context['images'] = ProductsImages.objects.filter(products=myproducts)
        context['realated'] = Products.objects.filter(catgory = myproducts.catgory)
        context['review'] = Reviw.objects.filter(products = myproducts)
        #context['review_count'] = Reviw.objects.all().annotate(product_count = Count('Proudct_Review'))
        return context
class BrandView(ListView):
    model = Brand

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = Brand.objects.all().annotate(product_count = Count('brand_product'))
        return context


class BrandDetail(DetailView):
    model = Brand
    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        context['brandc'] = Brand.objects.all().annotate(brand_count = Count('brand_product'))
        return  context 

class CatgoryList(ListView):
    model = Catgory
    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context['catgory'] = Catgory.objects.all().annotate(product_count = Count('Catgory_prodcut'))
        return context

from django.template.loader import render_to_string
from django.http import JsonResponse
def add_review(request,id):
    proucts =  Products.objects.get(id=id)
    if request.method == 'POST':
        form = ProudctReviewFrom(request.POST)
        if form.is_valid():
            myfrom = form.save(commit=False)
            myfrom.products = proucts
            myfrom.user = request.user
            myfrom.save()
            review = Reviw.objects.filter(products=proucts)
            html = render_to_string('include/reviews.html',{"review":review , request:request})
            return JsonResponse({"resulat":html})