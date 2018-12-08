from socket import *


#1.创建套接字
udpsocket = socket(AF_INET,SOCK_DGRAM)

#2.绑定地址,要两个括号，记住
Addr = udpsocket.bind(("",8890))

num = 1

while True:
    #3.接收数据
    revcData = udpsocket.recvfrom(1024)

    #4.返回数据
    udpsocket.sendto(revcData[0],revcData[1])

    print("----%d----"%num)
    num += 1