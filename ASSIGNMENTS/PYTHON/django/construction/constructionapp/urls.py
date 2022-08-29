from django.urls import path

import constructionapp.views
urlpatterns = [

    path('',constructionapp.views.home,name='join'),
    path('join/',constructionapp.views.join,name='join'),
    path('property/',constructionapp.views.property,name='join'),
    path('propertyhome/',constructionapp.views.propertyhome,name='phome')

]