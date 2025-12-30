from .models import Cart,Cart_Detail

# get or create cart
def get_context_process(request):
    cart , created= Cart.objects.get_or_create(user=request.user,status='inprogress')
    cart_detail=Cart_Detail.objects.filter(cart=cart)
    return {'cart_detail':cart_detail,'cart':cart}