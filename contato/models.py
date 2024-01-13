from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)


class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f'{self.name} '


class Contact(models.Model):
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        
    first_name = models.CharField(max_length=50,verbose_name='Nome')
    last_name = models.CharField(max_length=50,verbose_name='Sobrenome', blank=True)
    phone = models.CharField(max_length=50, verbose_name='Telefone')
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(verbose_name='Descrição',blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(verbose_name='Imagem', blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        blank = True,
        null = True
        )
        
    user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank = True,
        null = True
        )
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'