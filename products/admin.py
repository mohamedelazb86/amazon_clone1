from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Product,Brand,Product_Image,Review

class ProductImgageAdmin(admin.TabularInline):
    model=Product_Image

class ProductAdmin(SummernoteModelAdmin):
    list_display=['name','flag','price','quantity']
    list_filter=['flag','brand']
    search_fields=['name','subtitle','descriptions']

    inlines =[ProductImgageAdmin,]
    summernote_fields=('subtitle','descriptions')




admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Product_Image)
admin.site.register(Review)
