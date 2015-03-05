from django.conf.urls import patterns, include, url
from django.contrib import admin



urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/',  include('home.urls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
)