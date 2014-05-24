from django.conf.urls import patterns, include, url

from Website import views

urlpatterns = patterns('',
        url(r'^(?i)$', views.index, name='index'),)
