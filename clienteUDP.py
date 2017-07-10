#!/usr/bin/python
#-*- coding: utf-8 -*-

import socket

host = '192.168.0.1'
porta = 80

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #cria o objeto socket
s.sendto("AAABBBCCC",(host, porta)) #como não há conxão, apenas envia alguns dados.
data, addr = s.recvfrom(4096)
print data