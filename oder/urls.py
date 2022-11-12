from django.urls import path
from .views import add_to_cart , oder_list , cheakout
app_name = 'oder'
urlpatterns = [
    path('',oder_list,name='oder_list'),
    path('cheakout',cheakout,name='cheakout'),
    path('add-to-cart', add_to_cart , name="add_to_cart"),
]