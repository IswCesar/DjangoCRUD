from django.conf.urls import url

from . import views

app_name = 'CRUD'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^nuevo$', views.CreatePersona.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', views.UpdatePersona.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', views.DeletePersona.as_view(), name='delete'),
]