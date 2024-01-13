from django.contrib import admin
from django.urls import path
from contato import views

app_name ='contato'



urlpatterns = [
    path('<int:contact_id>/', views.contact, name="contato"),
    path('search/', views.search, name="search"),
    path('', views.index, name="index"),
    
]
