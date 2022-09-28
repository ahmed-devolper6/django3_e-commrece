from statistics import quantiles
from django.db import models
from utils.code_grente import grente_code
from django.utils import timezone
from django.contrib.auth.models import User 
from products.models import Products
# Create your models here.
STATUS_CART = (
    ('inprogecss','inprogecss'),
    ('compalted','compalted'),
)
class Carts(models.Model):
    user = models.ForeignKey(User , related_name='user_cart' , on_delete=models.SET_NULL , null=True )
    code = models.CharField(max_length=8 , default= grente_code)
    status = models.CharField(max_length=15 , choices= STATUS_CART)

class OderDeitl(models.Model):
    proudct = models.ForeignKey(Products , related_name='product_cart' , on_delete= models.CASCADE)
    cart = models.ForeignKey(Carts , related_name='cart_detail' , on_delete= models.SET_NULL , null=True , blank=True)
    quantiity = models.IntegerField()
    price = models.FloatField()
    
STATUS = (
    ('receieved','receieved'),
    ('processed','processed'),
    ('shiped','shiped'),
    ('delivered','delivered')
)
class Oders(models.Model):
    user = models.ForeignKey(User , related_name='user_oder' , on_delete=models.SET_NULL , null=True )
    code = models.CharField(max_length=8 , default= grente_code)
    oder_time = models.DateTimeField(default=timezone.now)
    deilevry_time = models.DateTimeField()
    status = models.CharField(max_length=15 , choices= STATUS)

class OderDeitl(models.Model):
    proudct = models.ForeignKey(Products , related_name='product_oder' , on_delete= models.CASCADE)
    oder = models.ForeignKey(Oders , related_name='oder_detail' , on_delete= models.SET_NULL , null=True , blank=True)
    quantiity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()