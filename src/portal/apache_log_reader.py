
import re

log = open('log_apache','r')
linhas = []

qtd_acesso = {}

for l in log:
  linhas.append(l)

re_data = re.compile('\d+\/\w+\/\d+')
re_hora = re.compile('\d\d\:\d\d\:\d\d')
re_url = re.compile('/site/\w.*')

for linha in linhas:
  colunas = linha.split(' ')
  if (len(colunas) < 20):
    continue

  url = re_url.findall(colunas[6])
  if len(url) == 0: continue
  print 'url'
  print url[0]
  if qtd_acesso.__contains__(url[0]):
    total = qtd_acesso[url[0]]
    qtd_acesso[url[0]] = (total+1)
  else:
    qtd_acesso[url[0]] = 1

  print 'IP Origem'
  print colunas[0]

  print 'data acesso'
  print re_data.findall(colunas[3])[0]

  print 'hora acesso'
  print re_hora.findall(colunas[3])[0]

  print 'verbo http'
  print colunas[5]

  print 'codigo http'
  print colunas[8]

  print 'navegador'
  print colunas[19]
  
for a in qtd_acesso:
  print str(a) +' - '+ str(qtd_acesso[a])
