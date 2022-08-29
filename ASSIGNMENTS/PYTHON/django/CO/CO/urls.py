
from django.contrib import admin
from django.urls import path
from conference_details.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('form/', FillForm, name='form'),
]
