from django.urls import path
from .views import *

urlpatterns = [
    path('user/', create_user),
    path('user/<int:id>/', get_user),
    path('login/<str:email>/', check_login),
    path('product/', product_list),
    path('product/find', search_product.as_view()),
    path('product/<int:pk>/', product_by_id),
    path('product/seller/<int:storeId>/', product_seller),
    path('product/find/<str:category>/', product_by_category),
    path('filter/rating/<int:rating>/', filter_rating),
    path('filter/condition/<str:condition>/', filter_condition),
    path('filter/price_and_rating/<int:minprice>/<int:maxprice>/<int:rating>/', filter_price_and_rating),
    path('filter/price_and_condition/<int:minprice>/<int:maxprice>/<str:condition>/', filter_price_and_condition),
    path('filter/rating_and_condition/<int:rating>/<str:condition>/', filter_rating_and_condition),
    path('filter/<int:minprice>/<int:maxprice>/<int:rating>/<str:condition>/', filter_all),
]