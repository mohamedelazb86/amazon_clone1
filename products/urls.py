from django.urls import path
from . import views

app_name='products'

urlpatterns = [
     # Brand
    path('all_brand',views.all_brand,name='all_brand'),
    
    # products
    path('',views.all_product,name='all_product'),
    path('<slug:slug>',views.product_detail,name='product_detail'),
    path('add_review/<slug:slug>',views.add_review,name='add_review'),

   
]
