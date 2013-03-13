from django.db import models

# Create your models here.

class Autore(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    def __unicode__(self):
        return u"%s %s" % (self.nome, self.cognome)
    class Meta:
        verbose_name_plural = "Autori"
    def nome_cognome(aut):
        return "%s %s" % (aut.nome.title(), aut.cognome.title())
        nome_cognome.short_description = 'Autore'

class Genere(models.Model):
    descrizione = models.CharField(max_length=30)
    def __unicode__(self):
        return self.descrizione
    class Meta:
        verbose_name_plural = "Genere"

class Libro(models.Model):
    titolo = models.CharField(max_length=200)
    autore = models.ForeignKey(Autore)
    genere = models.ForeignKey(Genere)
    data_acquisto = models.DateField(null=True, verbose_name="data di acquisto")
    def __unicode__(self):
        return self.titolo
    class Meta:
        verbose_name_plural = "Libri"

class Editore(models.Model):
    ragione_sociale = models.CharField(max_length=150)
    def __unicode__(self):
        return self.ragione_sociale
    class Meta:
        verbose_name_plural = "Editori"

class Articolo(models.Model):
    titolo = models.CharField(max_length=255, unique=True, db_index=True)
    genere = models.ForeignKey(Genere)
    testo = models.TextField(null=True, blank=True)
    data_pubblicazione = models.DateTimeField()
    autori = models.ManyToManyField(Autore)
    
    def __unicode__(self):
        return self.titolo
    class Meta:
        verbose_name_plural = "Articoli"
