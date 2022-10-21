from django.urls import path
from .views import ProudctView , ProudctDetail , BrandDetail , BrandView , CatgoryList , tester
from .api import  ProudctList , ProudctDetil_Api , CatgoryDetil_Api , BrandList_api , CatgoryList_api , BrandDetil_Api
app_name = 'products'
urlpatterns = [
    path('', ProudctView.as_view() , name="proudct_list"),
    path('test', tester , name="test"),
    path('<int:pk>', ProudctDetail.as_view() , name="Detail_list"),
    path('brand', BrandView.as_view() , name="brand_list"),
    path('brand/<int:pk>', BrandDetail.as_view() , name="brand_Detail"),
    path('catgory', CatgoryList.as_view() , name="catgory_list"),
    ####    API    ################
    path('api/proudct/', ProudctList.as_view()),
    path('api/proudct/<pk>', ProudctDetil_Api.as_view()),
    path('api/brand/', BrandList_api.as_view()),
    path('api/brand/<int:pk>', BrandDetil_Api.as_view()),
    path('api/catgory/', CatgoryList_api.as_view()),
    path('api/catgory/<int:pk>', CatgoryDetil_Api.as_view()),
]