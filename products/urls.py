from django.urls import path
from .views import ProudctView , ProudctDetail , BrandDetail , BrandView
app_name = 'products'
urlpatterns = [
    path('', ProudctView.as_view() , name="proudct_list"),
    path('<int:pk>', ProudctDetail.as_view() , name="Detail_list"),
    path('brand', BrandView.as_view() , name="proudct_list"),
    path('brand/<int:pk>', BrandDetail.as_view() , name="Detail_list"),

]