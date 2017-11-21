from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^materia/nueva/$', views.materia_nueva, name='materia_nueva'),
]
