from django.contrib import admin

from .models import Settings,Address,Delivery_Fee,Location
from django_summernote.admin import SummernoteModelAdmin

class SettingAdmin(SummernoteModelAdmin):
    list_display=['name','call_us','email_us']
   
    search_fields=['name','subtitle']
    summernote_fields=('subtitle',)
    


admin.site.register(Settings,SettingAdmin)
admin.site.register(Address)
admin.site.register(Delivery_Fee)
admin.site.register(Location)

