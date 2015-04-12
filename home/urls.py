from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.start, name='start'),
    # ex: /polls/5/
    
)