#from django.contrib.auth.decorators import login_required
#from django.contrib.auth import authenticate,  login,  logout
#from django.contrib.auth.models import User,  UserManager
from django.shortcuts import render_to_response
from models import Topico, Artigo, Noticia;
from posicao.gerador import gerador;
#from django.http import HttpResponse
#from django.http import HttpResponseRedirect
from django.template import RequestContext

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
    topico = Topico.objects.get(url=url)
    return render_to_response('topico.html',  {'topico' : topico},  context_instance=RequestContext(request));

def artigo(request, url):
    print url;
    artigo = Artigo.objects.get(url=url)
    return render_to_response('artigo.html',  {'artigo' : artigo},  context_instance=RequestContext(request));

def sobre(request):
    return render_to_response('sobre.html');