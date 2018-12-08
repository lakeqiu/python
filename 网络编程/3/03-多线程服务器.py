from socket import *
from threading import Thread

def serverclient(clientsocket,clientInfo):
    while True:
        # 5.接收客户端发来的数据
        print("-----2-----")
        revcData = clientsocket.recv(1024)
        if len(revcData) > 0:
            # 6.打印
            print("-----3-----")
            print("%s:%s" % (str(clientInfo), revcData.decode('gb2312')))
        else:
            # 7.关闭客户端套接字，不再为客户端服务
            print("%s已下线"%str(clientInfo))
            break

    clientsocket.close()


if __name__ == '__main__':
    #1.创建套接字
    tcpsocket = socket(AF_INET,SOCK_STREAM)

    #2.绑定地址
    tcpsocket.bind(('',8990))

    #3.变主动套接字为被动,括号里的数字表示最大可以同时接通多少个客户端
    tcpsocket.listen(5)

    while True:
        #4.等待连通（如果连通了返回一个新的套接字用于接收客户端信息，和客户端ip及端口）
        print("-----1-----")
        clientsocket,clientInfo = tcpsocket.accept()
        #创建多线程
        t = Thread(target=serverclient,args=(clientsocket,clientInfo))
        t.start()


    #8.关闭被动套接字（即关闭服务器）
    tcpsocket.close()