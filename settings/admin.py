from django.contrib import admin

from .models import Settings
from django_summernote.admin import SummernoteModelAdmin

class SettingAdmin(SummernoteModelAdmin):
    list_display=['name','call_us','email_us']
   
    search_fields=['name','subtitle']
    summernote_fields=('subtitle',)
    


admin.site.register(Settings,SettingAdmin)
