from django.urls import path
from .views import current_user, UserList
from . import views

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('', views.home),
    path('contact/', views.contact),
    path('orders/', views.orders), 
]