"""
created by Own, under the app [instagram]
"""

from django.conf import *
from django.urls import path
from . import views

urlpatterns = [
    path('home1/',views.home_view),
    path('crudops/', views.crudops),

]