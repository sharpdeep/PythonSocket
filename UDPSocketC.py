#coding=utf-8

import socket
HOST = 'localhost'
PORT = 8802
ADDR = (HOST,PORT)
BUFFSIZE = 1024

UDPcliSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    data = raw_input('>')
    if not data:
        break;
    UDPcliSocket.sendto(data,ADDR)
    datarecv,addr = UDPcliSocket.recvfrom(BUFFSIZE)
    if not datarecv:
        break
    print datarecv

UDPcliSocket.close()
