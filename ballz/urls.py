from ballz import settings
from django.conf.urls.defaults import patterns, include, url
from django.shortcuts import render_to_response, RequestContext
from django.contrib import admin

admin.autodiscover()


def landing(request):
    return render_to_response('landing.html', RequestContext(request, locals()))

urlpatterns = patterns('',
    url(r'^$', landing),
    url(r'^rosters/', include('ballz.rosters.urls')),
    url(r'^field_reservation/', include('ballz.field_reservation.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static_files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
