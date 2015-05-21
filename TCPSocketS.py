#coding=utf-8

import socket
import time
HOST = 'localhost'
PORT = 8081
BUFFSIZE = 1024
ADDR = (HOST,PORT)

serSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serSocket.bind(ADDR)
serSocket.listen(5)

while True:
    print "waiting for connection..."
    tcpCliSocket,addr = serSocket.accept()
    print '...connected from:',addr

    while True:
        data = tcpCliSocket.recv(BUFFSIZE)
        if not data:
            break
        tcpCliSocket.send('[%s] %s'%(time.ctime(),data))
        print [time.ctime()],":",data

tcpCliSocket.close()
serSocket.close()
