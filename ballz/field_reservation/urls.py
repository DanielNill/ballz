from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('field_reservation.views',
    url(r'^$', 'list_fields'),
    url(r'^create/', 'create_field'),
)
