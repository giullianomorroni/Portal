# -*- coding: utf-8 -*-
'''
Created on 03/09/2012

@author: giulliano
'''

import smtplib

class Mail(object):

    def send(self, message):
        fromaddr = 'morronigiulliano@gmail.com'
        toaddrs = 'giullianomorroni@gmail.com'
        subject = 'Você recebeu um comentário',
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, 'kama1234!')
        server.sendmail(fromaddr, toaddrs, 'To: {0}\nFrom: {1}\n\Subject: {2}\n\n{3}\n\n'.format(toaddrs, fromaddr, subject,message))
        server.close()
