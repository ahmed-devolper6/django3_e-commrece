from django.contrib import admin
from .models import Oders , OderDeitl , Cart , CartDeitl , Coupon
# Register your models here.
admin.site.register(Oders)
admin.site.register(OderDeitl)
admin.site.register(Cart)
admin.site.register(CartDeitl)
admin.site.register(Coupon)
