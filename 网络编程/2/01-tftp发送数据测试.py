from socket import *
import struct


sendData = struct.pack("!H8sb5sb",1,b"test.png",0,b"octet",0)

udpsocket = socket(AF_INET,SOCK_DGRAM)
udpsocket.sendto(sendData,("192.168.65.1",69))

udpsocket.close()