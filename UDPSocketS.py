#coding=utf-8

import socket
import time
HOST = 'localhost'
BUFFSIZE = 1024
PORT = 8802
ADDR = (HOST,PORT)

UDPSerSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
UDPSerSocket.bind(ADDR)
print('waiting for connect...')
while True:
    data,addr = UDPSerSocket.recvfrom(BUFFSIZE)
    print 'Received',data,'from',addr,'in [%s]'%time.ctime()
    UDPSerSocket.sendto('[%s]:%s'%(time.ctime(),data),addr)
    
UDPSerSocket.close()
    
