from django.db import models

class Image(models.Model): 
    name = models.CharField(max_length=255) 
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name 

class User(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    second_name = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    email_address = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ManyToManyField(Image)

    def __str__(self):
        return self.first_name + (' ') + self.second_name


class Rates(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE) 
    comment = models.CharField(max_length=150, null=True)
    stars = models.IntegerField(null=True)
    time = models.TimeField()

    def __str__(self):
        return str(self.userId)
    
class Reviews(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    image = models.ManyToManyField(Image)
    rate = models.ManyToManyField(Rates)

    def __str__(self):
        return self.name 

class Categories(models.Model):
    name = models.CharField(max_length=200, null=True) 

    def __str__(self):
        return self.name     

class Restaurants(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)
    image = models.ManyToManyField(Image)
    rate = models.ManyToManyField(Rates)

    def __str__(self):
        return self.name 
    
class Reservation2(models.Model):
    userId = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.IntegerField()
    comment = models.CharField(max_length=150, null=True)

    def __str__(self):
        return str(self.date)
