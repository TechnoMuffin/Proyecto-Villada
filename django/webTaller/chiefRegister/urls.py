from django.conf.urls import patterns, include, url

urlpatterns = patterns("",
                       url(r'^$', 'chiefRegister.views.nuevo_JefeArea', name="nuevo_JefeArea"),
                       url(r'^ingreso/$', 'chiefRegister.views.ingresar', name="ingreso"),
                       url(r'gracias/(?P<username>[\w]+)/$', 'chiefRegister.views.gracias_view', name='gracias')
)