from django.urls import path
from . import views

app_name='order'

urlpatterns = [
    path('',views.all_order,name='all_order'),
    path('checkout',views.checkout,name='checkout'),
]
