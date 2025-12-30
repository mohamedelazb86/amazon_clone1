from django.db import models
from authuser.models import User

class Settings(models.Model):
    name=models.CharField(max_length=120)
    logo=models.ImageField(upload_to='logo')
    subtitle=models.TextField(max_length=500)
    call_us=models.TextField(max_length=120)
    email_us=models.TextField(max_length=120)
    phones=models.TextField(max_length=120)
    address=models.TextField(max_length=200)
    facebook=models.URLField(null=True,blank=True)
    youtube=models.URLField(null=True,blank=True)
    android_apps=models.URLField(null=True,blank=True)
    ios_apps=models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name
    
class Location(models.Model):
    name=models.CharField(max_length=120)

    def __str__(self):
        return self.name
    
class Delivery_Fee(models.Model):
    location=models.ForeignKey(Location,related_name='fee_loction',on_delete=models.CASCADE)
    fee=models.IntegerField()
    
    def __str__(self):
        return str(self.fee)

TYPE_ADDRESS=[
    ('Home','Home'),
    ('Office','Office'),
    ('Others','Others'),
]
    
class Address(models.Model):
    user=models.ForeignKey(User,related_name='address_user',on_delete=models.CASCADE)
    address=models.CharField(max_length=120)
    type=models.CharField(max_length=120,choices=TYPE_ADDRESS)

    def __str__(self):
        return self.address

