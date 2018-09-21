from django.conf.urls import include, url
from django.contrib import admin
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

                  url(r'^$', views.post_list, name='post_list'),
                  url(r'^manga/new/$', views.manga_new, name='manga_new'),
                  url(r'^game/new/$', views.game_new, name='game_new'),
                  url(r'^manga/(?P<name>[0-9A-Za-z.\s_-]+)/$', views.manga_details, name='manga_details'),
                  url(r'^game/(?P<name>[0-9A-Za-z.\s_:-]+)/$', views.game_details, name='game_details'),
                  url(r'^create_post/$',views.create_post,name="create_post"),
                  url(r'^update/manga/(?P<name>[0-9A-Za-z.\s_:-]+)/$', views.update_manga, name='update_manga'),
                  url(r'^update/game/(?P<name>[0-9A-Za-z.\s_:-]+)/$', views.update_game, name='update_game'),
                  url(r'^delete/manga/(?P<name>[0-9A-Za-z.\s_:-]+)/$', views.delete_manga, name='delete_manga'),
                  url(r'^delete/game/(?P<name>[0-9A-Za-z.\s_:-]+)/$', views.delete_game, name='delete_game'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
