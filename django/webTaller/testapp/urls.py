from django.conf.urls import url, patterns
urlpatterns = patterns('',
                        url(r'^base$','testapp.views.base'),
                      )