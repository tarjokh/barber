from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.templatetags.rest_framework import data
from .serializers import *
from django.http import HttpResponse,JsonResponse
from rest_framework .parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework .views import APIView
from rest_framework import generics,filters
import os

@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):

    permission_classes = (permissions.IsAuthenticated)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def check_login(request, email_address):
    try:
        user = User.objects.filter(email_address=email_address)
    except:
        return HttpResponse(status=404) 

    if request.method == 'GET':
       serializer = UserSerializer(user,many=True)
       return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def get_user(request, id):
    try:
        user = User.objects.get(pk=id)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
       serializer = UserSerializer(user)
       return JsonResponse(serializer.data)

@csrf_exempt
def restaurants_list(request):
    if request.method == 'GET':
        restaurants = Restaurants.objects.all().order_by('name').reverse()
        serializer = RestaurantsSerializer(restaurants ,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RestaurantsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt 
def reservation_list(request): 
    if request.method == 'GET': 
        reservation = Reservation2.objects.all() 
        serializer = ReservationSerializer(reservation, many=True) 
        return JsonResponse(serializer.data, safe=False) 
 
    elif request.method == 'POST': 
        data = JSONParser().parse(request) 
        serializer = ReservationSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data, status=201) 
        return JsonResponse(serializer.errors, status=400) 
 
@csrf_exempt 
def reservation_list_detail(request): 
    if request.method == 'GET': 
        reservation = Restaurants.objects.all().order_by('id').reverse()
        serializer = ReservationSerializer(reservation) 
        return JsonResponse(serializer.data) 

    elif request.method == 'PUT': 
        data = JSONParser().parse(request) 
        serializer = ReservationSerializer(reservation, data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data) 
        return JsonResponse(serializer.errors, status=400) 
 
    elif request.method == 'POST': 
        data = JSONParser().parse(request) 
        serializer = ReservationSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data, status=201) 
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE': 
        reservation.delete() 
        return HttpResponse(status=204)
        
@csrf_exempt 
def reviews_list(request): 
    if request.method == 'GET': 
        reviews = Reviews.objects.all().order_by('id').reverse()
        serializer = ReviewsSerializer(reviews) 
        return JsonResponse(serializer.data) 

    elif request.method == 'PUT': 
        data = JSONParser().parse(request) 
        serializer = ReviewsSerializer(reviews, data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data) 
        return JsonResponse(serializer.errors, status=400) 

    elif request.method == 'POST': 
        data = JSONParser().parse(request) 
        serializer = ReviewsSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data, status=201) 
        return JsonResponse(serializer.errors, status=400)