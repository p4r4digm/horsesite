from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
	(r'^gitstats/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'srv/django/dapperhat/templates/dhsite/gitstats/' }),
	url(r'^$', 'dhsite.views.index'),
	url(r'^zendesk/$','dhsite.views.zendesk'),
)