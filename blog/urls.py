from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^$', views.post_list, name='post_list'),
    url(r'^manga/new/$', views.manga_new, name='manga_new'),
    url(r'^game/new/$', views.game_new, name='game_new'),
    url(r'^prova/$', views.prova, name='prova'),
    url(r'^manga/(?P<name>[0-9A-Za-z.\s_-]+)/$', views.manga_detail, name='manga_details'),
    url(r'^game/(?P<name>[0-9A-Za-z.\s_:-]+)/$', views.game_detail, name='game_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
