#coding = utf-8

import socket
import time

HOST = 'localhost'
PORT = 8081
BUFFSIZE = 1024
ADDR = (HOST,PORT)

TCPCliSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
TCPCliSocket.connect(ADDR)

while True:
    data = raw_input('>')
    if not data:
        break
    TCPCliSocket.send(data)
    data = TCPCliSocket.recv(BUFFSIZE)
    if not data:
        break
    print '%s'%data
