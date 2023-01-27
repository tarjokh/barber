from django.urls import path
from .views import current_user, CustomerAPIView

urlpatterns = [
    path('current_user/', current_user),
    path('users/', CustomerAPIView.as_view())
]