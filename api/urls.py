from django.urls import path
from .views import *

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('api/user/', create_user),
    path('user/', get_user),
    path('login/', check_login),
    path('make_order/', make_order),
]