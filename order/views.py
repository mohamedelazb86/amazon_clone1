from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Order,Order_Detail,Cart,Cart_Detail,Copoun
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from settings.models import Delivery_Fee
import datetime



@login_required
def all_order(request):
    orders=Order.objects.filter(user=request.user)
    paginator = Paginator(orders, 10)  # Show 2 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context={
        'page_obj':page_obj
    }
    return render(request,'order/order_list.html',context)

@login_required
def checkout(request):
    cart=Cart.objects.get(user=request.user,status='inprogress')
    cart_detail=Cart_Detail.objects.filter(cart=cart)
    delivery_fee=Delivery_Fee.objects.last().fee
    discount=0
    subtotal=cart.total_cart
    total=cart.total_cart + delivery_fee

    if request.method =='POST':
        copoun_code=request.POST.get('copoun_code')
        copoun=get_object_or_404(Copoun,code=copoun_code)

        if copoun and copoun.quantity > 0:
            today=datetime.datetime.today().date()
            if today >= copoun.start_date and today <= copoun.end_date :
                copoun_value=round(cart.total_cart / 100*copoun.discount,2)

                subtotal=cart.total_cart 
                discount=copoun_value
                total=round(subtotal+delivery_fee - copoun_value,2)

                context={
                    'cart':cart,
                    'cart_detail':cart_detail,
                    'subtotal':subtotal,
                    'delivery_fee':delivery_fee,
                    'discount':discount,
                    'total':total

                }
                return render(request,'order/checkout.html',context)




    context={
        'cart':cart,
        'cart_detail':cart_detail,
        'subtotal':subtotal,
        'delivery_fee':delivery_fee,
        'discount':discount,
        'total':total

    }
    return render(request,'order/checkout.html',context)