# -*- coding: utf-8 -*-
from django.db import models

class Topico(models.Model):
    def __unicode__(self):
        return self.titulo;
    titulo = models.CharField(max_length=250,  blank=False)
    url = models.CharField(max_length=250,  blank=False)

class Artigo(models.Model):
    def __unicode__(self):
        return self.titulo;
    titulo = models.CharField(max_length=250,  blank=False)
    descricao = models.TextField(max_length=2500,  blank=False)
    topico = models.ForeignKey(Topico,  blank=False)
    url = models.CharField(max_length=250,  blank=False)

class PalavraChave(models.Model):
    def __unicode__(self):
        return self.chave;
    topico = models.ForeignKey(Topico,  blank=False)
    chave = models.CharField(max_length=250,  blank=False)

class Comentario(models.Model):
    def __unicode__(self):
        return self.comentario;
    comentario = models.CharField(max_length=250,  blank=False)
    autor = models.CharField(max_length=250,  blank=True)
    ativo = models.IntegerField(default=1)
    artigo = models.ForeignKey(Artigo,  blank=False)

class Noticia(models.Model):
    def __unicode__(self):
        return self.descricao;
    descricao = models.CharField(max_length=250,  blank=False)