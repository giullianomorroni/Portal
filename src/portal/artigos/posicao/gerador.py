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
        opcoes.append('position:relative; top:20px; left:55px; height:20px; width:95px; font:24px arial, sans-serif;');
        opcoes.append('position:relative; top:40px; left:120px; height:20px; width:95px; font:20px arial, sans-serif;');
        opcoes.append('position:relative; top:60px; left:2000px; height:20px; width:95px; font:30px arial, sans-serif;');
        opcoes.append('position:relative; top:30px; left:300px; height:20px; width:95px; font:20px arial, sans-serif;');
        opcoes.append('position:relative; top:70px; left:320px; height:20px; width:95px; font:25px arial, sans-serif;');
        return opcoes;
