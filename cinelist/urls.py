from django.conf.urls import patterns, url

from cinelist import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)