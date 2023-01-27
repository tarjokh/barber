from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, logout
from django.shortcuts import redirect
from django.contrib import messages
from .serializers import UserSerializer, UserSerializerWithToken
from .models import *

"""
@api_view(['GET'])
def current_user(request):
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
"""

@api_view(['GET'])
def current_user(request):
    
    serializer = Customer(request.user)
    return Response(serializer.data)


class CustomerAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        lst = Customer.objects.all().values()
        return Response({'posts': list(lst)})
    
    def post(self, request):
        user = Customer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data, status=status.HTTP_201_CREATED)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


def registerpage(request):
    form = Customer()

    if request.method == 'POST':
        form = Customer(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['email_address']
            messages.success(request, 'Account Created Successfully for' + user)
            return redirect('loginpage')


def loginpage(request):
    if request.method == 'POST':
        email_address = request.POST['email_address']
        password = request.POST['password']
        user = authenticate(email_address = email_address, password = password)


def logoutpage(request):
    logout(request)
    return redirect('loginpage')