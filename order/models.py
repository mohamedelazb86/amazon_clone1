from django.db import models
from authuser.models import User
from utils.generate_code import generate_code
from django.utils import timezone
from products.models import Product
import datetime
from settings.models import Address,Delivery_Fee


STATUS_ODER=[
    ('recieved','تم استلام الطلب'),
    ('processed','تمت معالجة الطلب'),
    ('shipped','تم شحن الطلب'),
    ('delivered','تم تسليم الطلب'),
]
class Order(models.Model):
    user=models.ForeignKey(User,related_name='order_user',on_delete=models.SET_NULL,null=True,blank=True)
    code=models.CharField(max_length=75,default=generate_code)
    status=models.CharField(max_length=75,choices=STATUS_ODER)
    order_time=models.DateTimeField(default=timezone.now)
    delivery_time=models.DateTimeField(null=True,blank=True)
    delivery_address=models.ForeignKey(Address,related_name='address_user',on_delete=models.SET_NULL,null=True,blank=True)
    delivery_fee=models.ForeignKey(Delivery_Fee,related_name='order_fee',on_delete=models.SET_NULL,null=True,blank=True)
    total=models.FloatField(null=True,blank=True)
    copoun=models.ForeignKey('Copoun',related_name='order_copoun',on_delete=models.SET_NULL,null=True,blank=True)
    total_with_copoun=models.FloatField(null=True,blank=True)


    def __str__(self):
        return f'{self.user}----{self.code}'
    
    @property
    def order_detail_count(self):
        count_order=self.order_detail.all().count()
        return count_order
    
    
class Order_Detail(models.Model):
    order=models.ForeignKey(Order,related_name='order_detail',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='orderdetail_product',on_delete=models.CASCADE)
    price=models.FloatField()
    quantity=models.FloatField()
    total=models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.order)
    


class Copoun(models.Model):
    code=models.CharField(max_length=75)
    quantity=models.IntegerField()
    discount=models.FloatField()
    start_date=models.DateField()
    end_date=models.DateField(null=True,blank=True)
    

    def save(self,*args,**kwargs):
        if not self.end_date :
            week=datetime.timedelta(days=7)
            self.end_date=self.start_date + week
        super().save(*args,**kwargs)

    def __str__(self):
        return self.code

CART_STATUS=[
    ('inprogress','inprogress'),
    ('completed','completed'),
] 
class Cart(models.Model):

    user=models.ForeignKey(User,related_name='cart_user',on_delete=models.CASCADE)
    status=models.CharField(max_length=120,choices=CART_STATUS)
    copoun=models.ForeignKey(Copoun,related_name='cart_copoun',on_delete=models.SET_NULL,null=True,blank=True)
    total_with_copoun=models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.user)
    
    @property
    def total_cart(self):
        carts=self.cart_detail.all()
        total=0
        for item in carts:
            total +=item.total
        return total

class Cart_Detail(models.Model):
    cart=models.ForeignKey(Cart,related_name='cart_detail',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='catdetail_product',on_delete=models.CASCADE)
    quantity=models.FloatField(default=1)
    total=models.FloatField(null=True,blank=True)

    def __st__(self):
        return str(self.cart)