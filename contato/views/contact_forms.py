
from django.shortcuts import render, get_object_or_404, redirect
from contato.forms import ContactForm
from django.urls import reverse
from contato.models import Contact
from django.contrib.auth.decorators import login_required

@login_required(login_url='contato:login')   
def create(request):
    
    form_action = reverse('contato:create')
    
    if request.method == 'POST':      
        form = ContactForm(request.POST, request.FILES)    
             
        
        contexto = {        
            'form': form,
            'form_action': form_action,
            
        }
        
        if form.is_valid():            
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('contato:update', contact_id=contact.pk)
            
        return render(
            request, 
            'contato/create.html',
            contexto
        )
        
        
    contexto = {        
            'form': ContactForm(),
             'form_action': form_action,
        }
        
    return render(
        request, 
        'contato/create.html',
        contexto
    )        

@login_required(login_url='contato:login')       
def update(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
    )
    form_action = reverse('contato:update', args=(contact_id,))

    
    if request.method == 'POST':      
        form = ContactForm(request.POST,request.FILES, instance=contact)         
        
        contexto = {        
            'form': form,
            'form_action': form_action,
            
        }
        
        if form.is_valid():
            contact = form.save()
            return redirect('contato:update', contact_id=contact.pk)
            
        return render(
            request, 
            'contato/create.html',
            contexto
        )
        
        
    contexto = {        
            'form': ContactForm(instance=contact),
             'form_action': form_action,
        }
        
    return render(
        request, 
        'contato/create.html',
        contexto
    )            

@login_required(login_url='contato:login')   
def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
    )
    
    confirmation = request.POST.get('confirmation', 'no')
    print(f'Confirmation {confirmation}')
    
    if confirmation =='yes':
        contact.delete()
        return redirect('contato:index')
    
    return render(
        request,
        'contato/contato.html',
        {
            'contact':contact,
            'confirmation': confirmation
        }
    )
    