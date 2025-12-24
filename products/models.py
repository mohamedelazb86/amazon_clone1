from django.db import models
from django.utils.text import slugify
from authuser.models import User
from django.utils import timezone

FLAG_TYPE=[
    ('Sale','Sale'),
    ('New','New'),
    ('Feature','Feature'),
]
class Product(models.Model):
    name=models.CharField(max_length=120)
    image=models.ImageField(upload_to='image_product')
    sku=models.IntegerField()
    flag=models.CharField(max_length=25,choices=FLAG_TYPE)
    brand=models.ForeignKey('Brand',related_name='product_product',on_delete=models.SET_NULL,null=True,blank=True)
    slug=models.SlugField(null=True,blank=True)
    price=models.FloatField()
    subtitle=models.TextField(max_length=500)
    descriptions=models.TextField(max_length=5000)
    quantity=models.FloatField()

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    @property
    def review_count(self):
        reviews=self.review_product.all().count()
        
        return reviews
    
    @property
    def review_avg(self):
        reviews= self.review_product.all()

        total = 0
        if len(reviews) > 0:
            for item in reviews:
                total += item.rate
            avg = total / len(reviews)
        else:
            avg = 0
        return avg
        
         



    

class Product_Image(models.Model):
    product=models.ForeignKey(Product,related_name='product_image',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.product)
    

class Brand(models.Model):
    name=models.CharField(max_length=120)
    image=models.ImageField(upload_to='image_brand')
    slug=models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)

class Review(models.Model):
    user=models.ForeignKey(User,related_name='review_user',on_delete=models.SET_NULL,null=True,blank=True)
    product=models.ForeignKey(Product,related_name='review_product',on_delete=models.CASCADE)
    review=models.TextField(max_length=500)
    rate=models.IntegerField(choices=[(i,i) for i in range(1,6)])
    publish_date=models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{self.user}---{self.product}'


    
    
