from django.conf.urls.defaults import patterns, include, url
from rosters import views

urlpatterns = patterns('',
    url(r'^$', views.view_all_rosters),
    url(r'^create/', views.create_roster),
)
