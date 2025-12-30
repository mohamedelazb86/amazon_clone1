from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product,Review,Product_Image,Brand,Favorite
from django.core.paginator import Paginator
from order.models import Cart,Cart_Detail

@login_required
def all_product(request):
    products=Product.objects.all()
    paginator = Paginator(products, 20)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context={
        
        "page_obj": page_obj
    }
    return render(request,'products/all_product.html',context)

@login_required
def product_detail(request,slug):
    product=Product.objects.get(slug=slug)
    images=Product_Image.objects.filter(product=product)
    next_product=Product.objects.filter(id__gt=product.id).order_by('id').first()
    previous_product=Product.objects.filter(id__lt=product.id).order_by('-id').first()
    reviews=Review.objects.filter(product=product).order_by('-id')[:2]
    related_product=Product.objects.filter(brand=product.brand)

    context={
        'product':product,
        'images':images,
        'next_product':next_product,
        'previous_product':previous_product,
        'reviews':reviews,
        'related_product':related_product
    }
    return render(request,'products/product_detail.html',context)

def add_review(request,slug):
    product=Product.objects.get(slug=slug)
    if request.method =='POST':
        user=request.user
        review=request.POST.get('review')
        rate=request.POST.get('rating')

        Review.objects.create(
            user=user,
            product=product,
            review=review,
            rate=rate
        )
        return redirect('products:product_detail',slug=slug)
def add_favorite(request,id):
    product=get_object_or_404(Product,id=id)

    favorite ,created=Favorite.objects.get_or_create(user=request.user,product=product)

    if not created:
        favorite.delete()
    
    return redirect(request.META.get('HTTP_REFERER'))

def wish_all(request):
    products=Favorite.objects.filter(user=request.user)
    context={
        'products':products
    }
    return render(request,'products/wish_all.html',context)



# Brand
def all_brand(request):
    brands=Brand.objects.all()
    paginator = Paginator(brands, 25)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context={
        'page_obj':page_obj
    }
    return render(request,'products/all_brand.html',context)

def brand_detail(request,slug):
    brand=Brand.objects.get(slug=slug)

    products=Product.objects.filter(brand=brand)
    paginator = Paginator(products, 4)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context={
        'brand':brand,
        'page_obj':page_obj
    }
    return render(request,'products/brand_detail.html',context)

def add_to_cart(request):
    cart=Cart.objects.get(user=request.user,status='inprogress')

    product_id=request.POST.get('id')
    product=Product.objects.get(id=product_id)

    quantity=float(request.POST.get('quantity'))

    # انشاء تفاصيل الكارت أو احضاءر الموجودة سابقا
    cart_detail , created = Cart_Detail.objects.get_or_create(cart=cart,product=product)

    cart_detail.quantity=quantity
    cart_detail.total=cart_detail.quantity * product.price
    cart_detail.save()

    return redirect(request.META.get('HTTP_REFERER'))





