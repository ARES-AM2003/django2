from django.db import models
from django.contrib.auth.models import User
from order.models import Order
from home.models import Products
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL , null=True)
    quantity = models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    checked_out_at = models.DateTimeField(auto_now=True)