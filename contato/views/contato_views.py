from django.shortcuts import render, get_object_or_404, redirect
from contato.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.



def index(request):
    
    contacts = Contact.objects \
        .filter(show=True) \
        .order_by('-id')
    
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
   
    
    print(contacts.query)
    
    contexto = {
        'page_obj' : page_obj,
        'site_title': 'Contatos - '
        
    }
    
    return render(
        request, 
        'contato/index.html',
        contexto
    )
  
def search(request):
    
    search_value = request.GET.get('q', '').strip()
    
    if search_value =='':
        return redirect('contato:index')
    
    print(search_value)
    
    contacts = Contact.objects\
            .filter(show=True)\
            .filter(Q(first_name__icontains=search_value) |   
                    Q(last_name__icontains=search_value) |  
                    Q(email__icontains=search_value) | 
                    Q(phone__icontains=search_value)
                    )\
            .order_by('-id')
    
    print(contacts.query)
    
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
        
    contexto = {
        'page_obj' : page_obj,
        'site_title': 'Contatos - ',
        'search_value': search_value,
        
    }
    
    return render(
        request, 
        'contato/index.html',
        contexto
    )        

def contact(request, contact_id):
    
    # single_contact =  Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact.objects.filter(pk=contact_id, show =True))
    
    contact_name = f'{single_contact.first_name} {single_contact.last_name} - '
            
    contexto = {
        'contact' : single_contact,
        'site_title': contact_name
        
    }    
    return render(
        request, 
        'contato/contato.html',
        contexto
    )    