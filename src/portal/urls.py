from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

handler404 = 'artigos.views._404'

urlpatterns = patterns('',
    url(r'^$', 'artigos.views.home', name='home'),
    url(r'^topico/(?P<url>\w+)', 'artigos.views.topico', name='topico'),
    url(r'^artigo/(?P<url>\w+)', 'artigos.views.artigo', name='artigo'),
    url(r'^sobre/$', 'artigos.views.sobre', name='sobre'),
    url(r'^comentario/novo/$', 'artigos.views.novo_comentario', name='novo_comentario'),
    # url(r'^portal/', include('portal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
