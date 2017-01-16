from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^charindex/$', views.index, name='index'),
    url(r'^edit/(?P<id>\w+)/$', views.edit, name='edit'),
    url(r'^charsheet/(?P<id>\w+)/$', views.sheet, name='charsheet'),
    url(r'^create/$', views.create, name = 'create'),
    url(r'^delete/(?P<id>\w+)/$', views.delete, name = 'delete'),
]
