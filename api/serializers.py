from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'second_name', 'email_address', 'password', 'phone_number', 'date_created']


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    first_name = serializers.CharField(write_only=True)
    second_name = serializers.CharField(write_only=True)
    email_address = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(write_only=True)
    date_created = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        first_name = validated_data.pop('first_name', None)
        instance = self.Meta.model(**validated_data)
        if first_name is not None:
            instance.set_first_name(first_name)
        instance.save()
        return instance

    def create(self, validated_data):
        second_name = validated_data.pop('second_name', None)
        instance = self.Meta.model(**validated_data)
        if second_name is not None:
            instance.set_second_name(second_name)
        instance.save()
        return instance
    
    def create(self, validated_data):
        email_address = validated_data.pop('email_address', None)
        instance = self.Meta.model(**validated_data)
        if email_address is not None:
            instance.set_email_address(email_address)
        instance.save()
        return instance
    
    def create(self, validated_data):
        second_name = validated_data.pop('second_name', None)
        instance = self.Meta.model(**validated_data)
        if second_name is not None:
            instance.set_second_name(second_name)
        instance.save()
        return instance

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def create(self, validated_data):
        phone_number = validated_data.pop('phone_number', None)
        instance = self.Meta.model(**validated_data)
        if phone_number is not None:
            instance.set_phone_number(phone_number)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'id', 'first_name', 'second_name', 'email_address', 'password', 'phone_number', 'date_created')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'date_created', 'count_of_people', 'comment']

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name']

class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = ['id', 'name', 'category', 'address', 'url']