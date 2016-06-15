from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

#TODO Registro de Jefes de Area

def nuevo_JefeArea(request):
    if request.method=='POST':
            formulario = UserCreationForm(request.POST)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect('/')
    else:  
        formulario = UserCreationForm()
    return render_to_response('registerChief.html',{'formulario':formulario},context_instance=RequestContext(request))

def ingresar(request):
    if request.method=="POST":
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid():
                usuario=request.POST['username']
                clave=request.POST['password']
                acceso=authenticate(username=usuario, password=clave)
                if acceso is not None:
                    if acceso.is_active:
                        login(request,acceso)
                        return HttpResponseRedirect('/privado')
                    else:
                        return render_to_response('noactivo.html',context_instance=RequestContext(request))
                else:
                    return render_to_response('nousuario.html',context_instance=RequestContext(request))
        else:
            formulario=AuthenticationForm()
        return render_to_response('login.html',{'formulario':formulario},context_instance=RequestContext(request))