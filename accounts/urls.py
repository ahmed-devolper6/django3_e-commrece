from django.urls import path 
from .views import sginup , useractive , user_proflie
app_name = 'accounts'

urlpatterns = [
    path('sginup' , sginup , name='sginup'),
    path('<str:username>/acitve' , useractive , name='user_active'),
    path('profile/' , user_proflie , name='profile' )
]
