from django.db import models
from django.contrib.auth.models import User
from product.models import *


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    about = models.CharField(max_length=150,blank=True)
    profile_picture=models.ImageField(default='default.jpg',upload_to='profile_pictures')
    user_type=models.CharField(max_length=16,default='')
    def __str__(self):
        return self.user.username


class UserProfile(models.Model):
    user_type=models.CharField(max_length=16,default='')
    def __str__(self):
        return self.user.username



class Customer(models.Model):
    user_id = models.TextField(primary_key=True)
    user_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    delivary_address = models.CharField(max_length=150)

from customer.models import Customer

class Payment(models.Model):
    payment_method = models.TextField()
    payment_status = models.TextField()
    #due_payment = models.IntegerField()
    user_id = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)

