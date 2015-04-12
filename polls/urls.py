from django.conf.urls import patterns, url

from . import views, models


urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    #url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^category/(?P<category_name_url>\w+)$', views.category, name='category'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_url>\w+)/add_page/$', views.add_page, name='add_page'),
    url(r'^register/$', views.register, name='register'), 
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/$', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),# ADD NEW PATTERN!
    url(r'^(?P<library_id>\d+)/cart/$', views.cart, name='cart'),
    url(r'^(?P<library_id>\d+)/$', views.store, name='store'),
    url(r'^store/$', views.store, name='store'),
    url(r'^store/about/$', views.about, name='about'),
    url('polls/home/$', views.index, name='home'),
    url('polls/about/$', views.about, name='about'),
)

