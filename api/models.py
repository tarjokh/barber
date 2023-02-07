from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    second_name = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    email_address = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name + (' ') + self.second_name

class Order(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    count_of_people = models.FloatField(null=True)
    comment = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.date_created

class Categories(models.Model):
    name = models.CharField(max_length=200, null=True) 

    def __str__(self):
        return self.name    
        
class Places(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.ManyToManyField(Categories)
    address = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name 