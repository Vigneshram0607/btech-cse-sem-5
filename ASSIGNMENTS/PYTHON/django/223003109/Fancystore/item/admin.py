from django.contrib import admin
from .models import FancyStoreModel
# Register your models here.

# to register Admin interface
admin.site.register(FancyStoreModel)