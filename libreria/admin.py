from django.contrib import admin
from libreria.models import *
from django import forms
class LibroOption(admin.ModelAdmin):
    list_display = ('titolo', 'autore', 'genere', 'data_acquisto')
    date_hierarchy = 'data_acquisto'
    
class ArticoloOption(admin.ModelAdmin):
    fieldsets = (('Genere e data', {
        'fields' : (('genere', 'data_pubblicazione'),),
       # 'description : 'vuoi cercare su <a href="http://www.google.com">Google</a>?',
        'classes' : ('collapse',),
        }),('', {'fields' : ('titolo', 'testo', 'autori'),}))
    fieldsets = (('Dettagli', {
        'fields' : (('titolo', 'testo', 'autori'),),
       # 'description : 'vuoi cercare su <a href="http://www.google.com">Google</a>?',
        'classes' : ('collapse',),
        }),('', {'fields' : ('genere', 'data_pubblicazione'),}))

class AutoreOption(admin.ModelAdmin):
    search_fields  = ('cognome', 'nome')
                                    

admin.site.register(Genere)
admin.site.register(Editore)
admin.site.register(Libro, LibroOption)
admin.site.register(Autore, AutoreOption)
admin.site.register(Articolo, ArticoloOption)
