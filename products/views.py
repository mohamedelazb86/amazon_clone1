from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product,Review,Product_Image
from django.core.paginator import Paginator

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

