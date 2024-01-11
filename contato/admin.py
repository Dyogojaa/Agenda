from django.contrib import admin
# from .models import Contact
from contato import models

# Register your models here.
@admin.register(models.Contact)
class ContatoAdmin(admin.ModelAdmin):
    ...