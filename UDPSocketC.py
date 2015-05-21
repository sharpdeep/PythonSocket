#coding=utf-8
import socket
port = 8802
host='localhost'

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(b'hello,this is a test info !',(host,port))
