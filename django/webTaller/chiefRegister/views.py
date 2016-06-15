from django.shortcuts import render
from .forms import RegistroUserForm

def nuevo_JefeArea(request):
    if request.method == 'POST':
        formulario = RegistroUserForm(request.POST)
    else:
        formulario = RegistroUserForm()
    context = {
        'form': formulario
    }
    return render(request, 'registerChief.html', context)