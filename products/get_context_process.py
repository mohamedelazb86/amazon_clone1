from .models import Favorite

def get_favorite(request):
    products=Favorite.objects.all()
    return {'product_favorites':products}