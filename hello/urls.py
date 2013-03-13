from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'hello.views.home', name='home'),
    #url(r'^hello/', include('hello.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #(r'^hello/$', "hello.views"),
    (r'^libri/$', "libreria.views.libri"),
    (r'^libri/(\d+)/$', "libreria.views.libro"),
    (r'^libri/acquistati/(?P<anno>\d{4})/(?P<mese>\d{1,2})/$', "libreria.views.libri_per_data_acquisto"),
    (r'^libri/autori/(?P<nome>)/$', "libreria.views.libri_autore"),
    (r'^libri/generi/(\d+)/$', "libreria.views.libri_genere"),
    (r'^libri/ricerca/$', "libreria.views_wiki.ricerca"),
    (r'^test/$', 'libreria.views.test'),
    url(r'^autori/(?P<id>\d+)/$', 'libreria.views.autore_dettaglio', name='dettaglio_autore_id'),
    url(r'^autori/(?P<cognome>[a-zA-Z]\w*)/$', 'libreria.views.autore_dettaglio', name='dettaglio_autore_cognome'),
)
#urlpatterns += patterns('libreria.views_articoli',
#    (r'^articoli/1971/$', 'speciale_dna'),
#    (r'^articoli/(\d{4})/$', 'archivio_anno'),
#    (r'^articoli/(?P<anno>\d{4})/(?P<mese>\d{2})/$', 'archivio_mese'),
#    (r'^articoli/(?P<anno>\d{4)}/(?P<mese>\d{2})/(\d+)/$', 'articolo'),
#)


