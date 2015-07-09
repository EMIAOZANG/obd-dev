"""diag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^show_info/([^\#]+)$','expose.views.show_url_info_NB', name='show_url_info_NB'),
    url(r'^show_info/$','expose.views.show_url_info',name='show_url_info'),
    url(r'^$','expose.views.index',name='home'), #url pattern for app name expose 
    url(r'^contact\S+/$','contact.views.index',name='contact_index'),
)
