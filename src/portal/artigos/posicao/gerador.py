'''
Created on 14/06/2012
@author: giulliano
'''

from collections import deque;

class gerador:

    global opcoes;

    def __init__(self):
        print 'Gerador de posicoes';




    def gerar(self):
        opcoes = deque();    
        opcoes.append('position:absolute; top: 230px; left: 600px; font: 25px arial, sans-serif;');
        opcoes.append('position:absolute; top: 160px; left: 250px; font: 26px arial, sans-serif;');
        opcoes.append('position:absolute; top: 080px; left: 000px; font: 25px arial, sans-serif;');
        opcoes.append('position:absolute; top: 040px; left: 420px; font: 23px arial, sans-serif;');
        return opcoes;
