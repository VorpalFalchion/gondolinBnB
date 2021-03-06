"""gondolinbnb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from clientcolony import views as clientcolony_views
from charsheet import views as charsheet_views
from clientcolony.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', clientcolony_views.login, name='login'),
    #url(r'^sheet/', charsheet_views.sheet, name='sheet'),
    url(r'', include('clientcolony.urls')),
    url(r'', include('charsheet.urls')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', clientcolony_views.logout_view, name='logout'),
    url(r'^login/new_user/$', clientcolony_views.new_user, name='new_user'),
]
