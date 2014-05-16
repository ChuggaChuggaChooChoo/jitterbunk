from django.conf.urls import patterns, url

from bunk import views

urlpatterns = patterns(
    '',
    url(r'^$', views.bunkFeed, name='feed'),
    url(r'^(?P<user_id>\d+)/$', views.personalBunkFeed, name='personalFeed'),
    url(r'^(?P<user_id>\d+)/add/$', views.bunkem, name='bunkem'),
)
