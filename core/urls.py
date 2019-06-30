from django.urls import path 
from . import views 


urlpatterns  = [
    path('register/' , views.register , name = 'register'),
    path('profile/<str:username>' , views.profile , name = 'profile'),
    path('update_profile/' , views.update_profile , name = 'update_profile'),
    path('update_profile_confirm/' , views.update_profile_confirm , name = 'update_profile_confirm'),
]