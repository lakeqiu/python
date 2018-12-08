import time
import gevent

#使用gevent，那么套接字socket就要使用其的，才不会堵塞
from gevent import socket,monkey

#必写，她会改变后面写的代码，变为gevent里的某一些
monkey.patch_all()

#为客户端服务的套接字
def clientserver(clientsocket):
    while True:
        #在还没收到数据的情况下，这个协程（耗时操作）会跟server（）里的耗时操作轮流交换操作
        data = clientsocket.recv(1024)

        if not data:
            clientsocket.close()
        print(data.decode('gb2312'))
        clientsocket.send(data)


def server():
    #创建套接字
    tcpsocket = socket.socket()

    tcpsocket.bind(('',9999))
    tcpsocket.listen(5)
    while True:
        #两个耗时操作
        clientsocket,addre = tcpsocket.accept()
        gevent.spawn(clientserver,clientsocket)


if __name__ == '__main__':
    server()