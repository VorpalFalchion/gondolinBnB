from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^charindex/$', views.index, name='index'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^charsheet/(?P<id>\w+)/', views.sheet, name='charsheet'),
]
