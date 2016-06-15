from django.conf.urls import patterns, include, url

urlpatterns = patterns("",
                       url(r'^registrar_jefe_area/$','chiefRegister.views.nuevo_JefeArea', name="nuevo_JefeArea"),
                       url(r'^ingreso/$','chiefRegister.views.ingresar', name="ingreso")
)