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
        opcoes.append('position:absolute; top: 040px; left: 420px; font: 23px arial, sans-serif;');
        opcoes.append('position:absolute; top: 080px; left: 000px; font: 25px arial, sans-serif;');
        opcoes.append('position:absolute; top: 120px; left: 602px; font: 23px arial, sans-serif;');
        opcoes.append('position:absolute; top: 240px; left: 550px; font: 26px arial, sans-serif;');
        opcoes.append('position:absolute; top: 280px; left: 50px; font: 25px arial, sans-serif;');
        opcoes.append('position:absolute; top: 330px; left: 400px; font: 25px arial, sans-serif;');
        return opcoes;
