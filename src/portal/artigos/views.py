#-*- coding: utf-8 -*-

#from django.contrib.auth.decorators import login_required
#from django.contrib.auth import authenticate,  login,  logout
#from django.contrib.auth.models import User,  UserManager
from django.shortcuts import render_to_response
from models import Topico, Artigo, Noticia, Comentario, PalavraChave;
from posicao.gerador import gerador;
from django.core.paginator import Paginator, InvalidPage, EmptyPage
#from django.http import HttpResponse
#from django.http import HttpResponseRedirect
from django.template import RequestContext
#from ubuntuone.storageprotocol.errors import DoesNotExistError
from portal.mail import Mail

def _404(request):
    return render_to_response('404.html');

def _500(request):
    return render_to_response('500.html');

def home(request):
    topicos = Topico.objects.all();
    noticias = Noticia.objects.all();
    
    artigos = Artigo.objects.all(); #trazeer os mais lidos
    artigos_pg = Paginator(artigos, 10)

    try:
        page = int(request.GET.get('p', '1'))
    except ValueError:
        page = 1

    try:
        artigos = artigos_pg.page(page)
    except (EmptyPage, InvalidPage):
        artigos = artigos_pg.page(artigos_pg.num_pages)

    return render_to_response('home.html', {'topicos':topicos, 'noticias':noticias, 'artigos':artigos});

def topico(request, url):
    try:
        topico = Topico.objects.get(url=url)
        artigos = Artigo.objects.all(); #trazeer os mais lidos
    except Topico.DoesNotExist:
        return _404(request);
    palavras = PalavraChave.objects.filter(topico=topico);
    p = ''
    for palavra in palavras:
        p += palavra.chave + ','

    return render_to_response('topico.html',  {'topico':topico, 'palavras':palavras, 'artigos':artigos, 'p':p},  context_instance=RequestContext(request));

def artigo(request, url):
    comentarios = ['Nenhum comentario'];
    try:
        artigo = Artigo.objects.get(url=url)
        comentarios = Comentario.objects.filter(artigo = artigo.id);
    except Comentario.DoesNotExist:
        print 'nenhum comentario';
    except Artigo.DoesNotExist:
        return _404(request)    
    total_com = len(comentarios);
    return render_to_response('artigo.html',  {'artigo' : artigo, 'comentarios':comentarios, 'total_com': total_com},  context_instance=RequestContext(request));

def sobre(request):
    return render_to_response('sobre.html');

def novo_comentario(request):
    try:
        c = Comentario();
        c.autor = request.POST['autor'];
        c.comentario = request.POST['comentario'];
        artigo = Artigo.objects.get(id = request.POST['id_artigo']);
        m = Mail()
        m.send('O artigo %s recebeu um comentário, corre lá...' %artigo.titulo)
    except Artigo.DoesNotExist:
        return _404(request)
    c.artigo = artigo;
    c.save();
    comentarios = Comentario.objects.filter(artigo = artigo.id)
    return render_to_response('artigo.html',  {'artigo' : artigo, 'comentarios':comentarios},  context_instance=RequestContext(request));