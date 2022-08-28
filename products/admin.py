from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class proudcutimageinline(admin.TabularInline):
    model = ProductsImages
class ProductModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display =  ['name' ,  'flags'  ]
    inlines = [proudcutimageinline]


    
admin.site.register(Products , ProductModelAdmin)
admin.site.register(ProductsImages)
admin.site.register(Catgory)
admin.site.register(Brand)
admin.site.register(Reviw)