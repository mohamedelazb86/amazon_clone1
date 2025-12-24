from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product,Review

@login_required
def all_product(request):
    products=Product.objects.all()

    
    context={
        'products':products
    }
    return render(request,'products/all_product.html',context)

@login_required
def product_detail(request,slug):
    product=Product.objects.get(slug=slug)
    context={
        'product':product
    }
    return render(request,'products/product_detail.html',context)
