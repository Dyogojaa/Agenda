from django.shortcuts import render
from contato.forms import RegisterForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

    return render(
        request,
        'contato/register.html',
        {
            'form': form
        }
    )