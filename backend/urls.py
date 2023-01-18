from rest_framework_jwt.views import obtain_jwt_token
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from graphene_django.views import GraphQLView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token-auth/', obtain_jwt_token),
    path('', include('core.urls')),
    path("graphql", GraphQLView.as_view(graphiql=True)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
