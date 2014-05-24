from django.conf.urls import patterns, include, url

import Website

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AlmostThere.views.home', name='home'),
    # url(r'^AlmostThere/', include('AlmostThere.AlmostThere.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Routes to the website
    url(r'^Website/', include('Website.urls', namespace='Website')),

    # Routes index to website
    url(r'^/', include('Website.urls', namespace='Website')),
)
