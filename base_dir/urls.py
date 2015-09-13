"""base_dir URL Configuration

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
from news.views import ArticlesList

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^articles/(?P<year>[0-9]{4})/$',ArticlesList.as_view(),name='articles-list-year_wise'),
    url(r'^articles/$',ArticlesList.as_view(),name='articles-list'),
    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-1]{1}[0-9]{1})/$',ArticlesList.as_view(),name='articles-list-month_wise'),
]
