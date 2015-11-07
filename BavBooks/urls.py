"""BavBooks URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$','Books.views.Home' ),
    url(r'^WriteWithUs/','Books.views.WriteWithUs' ),
    url(r'^get/(?P<book_id>\d+)/$','Books.views.MyBook' ),
    url(r'^Categories/(?P<Categor>\S+)/$','Books.views.Categories' ),
    url(r'^CCategories/(?P<Categor>\S+)/$','Books.views.Sub_Categories' ),
    url(r'^login/','Authentication.views.login' ),
    url(r'^loggedout/','Authentication.views.loggedout'),
    url(r'^register/','Authentication.views.register'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reset/$', 'Authentication.views.reset', name='reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'Authentication.views.reset_confirm', name='password_reset_confirm'),
    url(r'^success/$', 'Authentication.views.success', name='success'),
    url(r'^reset_success/$', 'Authentication.views.reset_success', name='reset_success'),
    url(r'^download/(?P<download_link>\S+)/$','Books.views.download' ),
    url(r'^search/','Books.views.search_titles'),
    
]
