from django.urls import path
from .views import ProudctView , ProudctDetail , BrandDetail , BrandView , CatgoryList , tester
app_name = 'products'
urlpatterns = [
    path('', ProudctView.as_view() , name="proudct_list"),
    path('test', tester , name="test"),
    path('<int:pk>', ProudctDetail.as_view() , name="Detail_list"),
    path('brand', BrandView.as_view() , name="brand_list"),
    path('brand/<int:pk>', BrandDetail.as_view() , name="brand_Detail"),
    path('catgory', CatgoryList.as_view() , name="catgory_list"),

]