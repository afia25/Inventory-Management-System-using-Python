from django.contrib import admin

# Register your models here.
from .models import Products
admin.site.register(Products)


from .models import CustomerInfo
admin.site.register(CustomerInfo)

from .models import Invoice
admin.site.register(Invoice)

from .models import Sales
admin.site.register(Sales)

from .models import SupplierInfo
admin.site.register(SupplierInfo)
