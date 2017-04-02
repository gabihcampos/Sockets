#!/usr/bin/env python
# -*- coding: utf-8 -*-

# adaptado de https://wiki.python.org/moin/TcpCommunication

import socket
import sys

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = ''

for i in range(1,len(sys.argv)):
    MESSAGE += sys.argv[i]
    MESSAGE += ' '

print ("[CLIENTE] Iniciando")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("[CLIENTE] Conectando")
s.connect((TCP_IP, TCP_PORT))
print ("[CLIENTE] Enviando dados: \"" + MESSAGE + "\"")
s.send(MESSAGE.encode('utf-8'))
print ("[CLIENTE] Recebendo dados do servidor")
data = s.recv(BUFFER_SIZE)
print ("[CLIENTE] Dados recebidos em resposta do servidor: \"" + data.decode('utf-8') + "\"")
print ("[CLIENTE] Fechando conexão com o servidor")
s.close()

print ("[CLIENTE] Fim")
