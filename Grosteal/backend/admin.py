from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderDetails)
admin.site.register(Users)

