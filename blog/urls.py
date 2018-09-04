from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^$', views.post_list, name='post_list'),
    url(r'^fumetto/new/$', views.manga_new, name='manga_new'),
    url(r'^game/new/$', views.game_new, name='game_new'),
    url(r'^prova/$', views.prova, name='prova'),
    url(r'^(?P<name>[0-9A-Za-z.\s_-]+)/$', views.post_detail, name='post_details'),


]
