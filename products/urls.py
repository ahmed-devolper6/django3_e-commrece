from django.urls import path
from .views import ProudctView , ProudctDetail
appname = 'products'
urlpatterns = [
    path('', ProudctView.as_view() , name="proudct_list"),
    path('<int:pk>', ProudctDetail.as_view() , name="Detail_list"),
]