#coding = utf-8

import socket
import time

HOST = 'localhost'
PORT = 8081
BUFFSIZE = 1024
ADDR = (HOST,PORT)

cliSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliSocket.connect(ADDR)

while True:
    data = raw_input('>')
    if not data:
        break
    cliSocket.send(data)
    data = cliSocket.recv(BUFFSIZE)
    if not data:
        break
    print '%s'%data
