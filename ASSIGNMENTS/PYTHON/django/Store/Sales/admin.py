from django.contrib import admin
from .models import Sale, Store, Product

# Register your models here.
admin.site.register(Sale)
admin.site.register(Store)
admin.site.register(Product)