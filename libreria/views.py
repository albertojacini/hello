# Create your views here.
from django.template import Context, loader 
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponse, Http404
from models import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

def autore_dettaglio(request, id=None, cognome=None):

    if id:
        autore = get_object_or_404 (Autore, pk=id)
    elif cognome:
        autore = get_object_or_404(Autore, cognome__iexact=cognome)
    libri = autore.libro_set.all()
    preferiti = request.session.get('preferiti', [])
    if request.method == "POST":
        for libro in libri:
            if libro.pk in preferiti:
                preferiti.remove(libro.pk)
        for libro_pk in request.POST.getlist('libro_pk'):
            preferiti.append(int(libro_pk))
        request.session['preferiti'] = preferiti
    return render_to_response('autore.html', {'autore':autore, 
        'libri': [(libro, libro.pk in preferiti)for libro in libri],
        'preferiti': Libro.objects.in_bulk(preferiti).values()}, context_instance=RequestContext(request))

def libri(request):
    return render_to_response('libri.html', {
        'libri': Libro.objects.all().order_by('autore__cognome')
        })

def libro(request, id):
    try:
        libro = Libro.objects.get(pk=id)
        return HttpResponse("'%s' di %s, %s<br>" % (libro.titolo, libro.autore, libro.genere))
    except Libro.DoesNotExist:
        return HttpResponse("Codice %s inesistente" % id)


def libri_per_data_acquisto(request, mese, anno):
    libri = Libro.objects.filter(data_acquisto__year=int(anno))
    libri = libri.filter(data_acquisto__month=int(mese))
    elenco = ""
    for libro in libri.order_by('titolo'):
        elenco += "'%s' di %s, %s<br>" % (libro.titolo,
                                      libro.autore, libro.genere)
    if elenco == "":
        elenco = "Nessun libro"
    return HttpResponse(elenco)


def libri_genere(request, id):
    genere = get_object_or_404(Genere, pk=id)
    return render_to_response('libri.html', {
        'libri': Libro.objects.filter( genere=genere).order_by('titolo'),
        'genere': genere,})

def libri_autore(request, id):
    autore = get_object_or_404(Autore, pk=id)
    return render_to_response('libri.html', {
        'libri': Libro.objects.filter(autore=autore).order_by('titolo'),
        'autore': autore,})
    
def test(request):
    return render_to_response('test.html', {'request': 'request', 
    })