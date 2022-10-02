from django.urls import path
from .views import ProudctView , ProudctDetail , BrandDetail , BrandView , CatgoryList , tester
from .api import proudct_list_api , proudct_detail_api , ProudctList , Proudctdetil_api
app_name = 'products'
urlpatterns = [
    path('', ProudctView.as_view() , name="proudct_list"),
    path('test', tester , name="test"),
    path('<int:pk>', ProudctDetail.as_view() , name="Detail_list"),
    path('brand', BrandView.as_view() , name="brand_list"),
    path('brand/<int:pk>', BrandDetail.as_view() , name="brand_Detail"),
    path('catgory', CatgoryList.as_view() , name="catgory_list"),


    ####    API    ################
    path('api/', proudct_list_api ),
    path('api/<int:id>', proudct_detail_api ),
    path('api_g/', ProudctList.as_view()),
    path('api_g/<pk>', Proudctdetil_api.as_view()),


]