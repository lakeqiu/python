from socket import *

#1.创建一个套接字
udpsocket = socket(AF_INET,SOCK_DGRAM)

#2.绑定端口
udpAddr = udpsocket.bind(('',10000))

while True:
    #3.接受数据并解包
    recvData = udpsocket.recvfrom(1024)
    content,destInfo = recvData

    #4.打印数据
    print("%s:%s"%(destInfo,content.decode('gb2312')))