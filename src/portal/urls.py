from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'portal.artigos.views.home', name='home'),
    url(r'^topico/(?P<url>\w+)', 'portal.artigos.views.topico', name='topico'),
    url(r'^artigo/(?P<url>\w+)', 'portal.artigos.views.artigo', name='artigo'),
    url(r'^sobre/$', 'portal.artigos.views.sobre', name='sobre'),
    # url(r'^portal/', include('portal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
