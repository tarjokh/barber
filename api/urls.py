from django.urls import path
from .views import *

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('api/user/', create_user),
    path('user/', get_user),
    path('login/', check_login),
    path('restaurants/', restaurants_list),
    path('reservation/', reservation_list), 
    path('reservation_detail/', reservation_list_detail),
    path('reviews_list/', reviews_list),
]