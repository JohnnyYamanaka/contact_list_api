from django.conf.urls import url
from . import views
from django.urls import path, include


urlpatterns = [

    path('', views.Contactlist.as_view(), name = 'contact-list'),

]
