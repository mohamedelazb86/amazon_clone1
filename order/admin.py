from django.contrib import admin

from .models import Order,Order_Detail,Copoun,Cart,Cart_Detail

admin.site.register(Order)
admin.site.register(Order_Detail)
admin.site.register(Copoun)
admin.site.register(Cart)
admin.site.register(Cart_Detail)