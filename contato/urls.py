from django.contrib import admin
from django.urls import path
from contato import views

app_name ='contato'



urlpatterns = [
    
    path('', views.index, name="index"),
    path('search/', views.search, name="search"),
    
    # Contato (CRUD)
    path('contato/<int:contact_id>/detail/', views.contact, name="contato"),
    path('contato/<int:contact_id>/update/', views.update, name="update"),
    path('contato/<int:contact_id>/delete/', views.delete, name="delete"),
    path('contato/create/', views.create, name="create"),
    
    # Register (CRUD)    
    path('user/create/', views.register, name="register"),
    
        
]
