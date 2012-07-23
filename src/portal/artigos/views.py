#-*- coding: utf-8 -*-

#from django.contrib.auth.decorators import login_required
#from django.contrib.auth import authenticate,  login,  logout
#from django.contrib.auth.models import User,  UserManager
from django.shortcuts import render_to_response
from models import Topico, Artigo, Noticia, Comentario, PalavraChave;
from posicao.gerador import gerador;
#from django.http import HttpResponse
#from django.http import HttpResponseRedirect
from django.template import RequestContext
from ubuntuone.storageprotocol.errors import DoesNotExistError

def _404(request):
    return render_to_response('404.html');

def home(request):
    topicos = Topico.objects.all();
    noticia = Noticia.objects.all();
    ttl = len(noticia);
    if ttl == 0:
        noticia = ['Sem novidade...'];
        ttl=1;
    p = gerador();
    opcoes = p.gerar();
    return render_to_response('home.html', {'topicos':topicos, 'noticia':noticia[ttl-1], 'opcoes':opcoes});

def topico(request, url):
    try:
        topico = Topico.objects.get(url=url)
    except Topico.DoesNotExist:
        return _404(request);
    palavras = PalavraChave.objects.filter(topico=topico);
    return render_to_response('topico.html',  {'topico' : topico, 'palavras' : palavras},  context_instance=RequestContext(request));

def artigo(request, url):
    artigo = Artigo.objects.get(url=url)
    comentarios = ['Nenhum comentario'];
    try:
        comentarios = Comentario.objects.filter(artigo = artigo.id);
    except Comentario.DoesNotExist:
        print 'nenhum comentario';
    total_com = len(comentarios);
    return render_to_response('artigo.html',  {'artigo' : artigo, 'comentarios':comentarios, 'total_com': total_com},  context_instance=RequestContext(request));

def sobre(request):
    return render_to_response('sobre.html');

def novo_comentario(request):
    c = Comentario();
    c.autor = request.POST['autor'];
    c.comentario = request.POST['comentario'];
    artigo = Artigo.objects.get(id = request.POST['id_artigo']);
    print artigo.id; 
    c.artigo = artigo;
    c.save();
    comentarios = Comentario.objects.filter(artigo = artigo.id)
    return render_to_response('artigo.html',  {'artigo' : artigo, 'comentarios':comentarios},  context_instance=RequestContext(request));