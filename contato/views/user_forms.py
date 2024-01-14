from django.shortcuts import redirect, render
from contato.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def register(request):
    
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():    
            form.save()
            messages.success(request, 'Usuário Registrado com Sucesso!')
            return redirect('contato:login')

    return render(
        request,
        'contato/register.html',
        {
            'form': form
        }
    )
    
def login_view(request):
    
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():    
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('contato:index')        
        messages.error(request, 'Senha ou Usuário Inválido!')
            
    return render(
        request,
        'contato/login.html',
        {
            'form': form
        }
    )
    
@login_required(login_url='contato:login')   
def logout_view(request):
    auth.logout(request)
    messages.success(request, 'Deslogado com sucesso!')
    return redirect('contato:login')

@login_required(login_url='contato:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contato/user_update.html',
            {
                'form': form
            }
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contato/user_update.html',
            {
                'form': form
            }
        )

    form.save()
    return redirect('contato:user_update')