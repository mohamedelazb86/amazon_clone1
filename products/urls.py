from django.urls import path
from . import views

app_name='products'

urlpatterns = [
     # Brand
    path('all_brand',views.all_brand,name='all_brand'),
    path('brand_detail/<slug:slug>',views.brand_detail,name='brand_detail'),
    path('wish_all',views.wish_all,name='wish_all'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    

    # products
    path('',views.all_product,name='all_product'),
    path('<slug:slug>',views.product_detail,name='product_detail'),
    path('add_review/<slug:slug>',views.add_review,name='add_review'),
    path('add_favorite/<int:id>',views.add_favorite,name='add_favorite'),

    

   
]
