from django.conf.urls.defaults import patterns, url
from rosters import views

urlpatterns = patterns('',
    url(r'^$', views.view_all_rosters),
    url(r'^create/$', views.create_roster),
    url(r'^manage/(?P<team_id>\d+)/$', views.manage_roster),
    url(r'^add_player/', views.add_player),
    url(r'^remove_player/', views.remove_player)
)
