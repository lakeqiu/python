from socket import *
from threading import Thread
import datetime

#这个方法好一点
udpsocket = None

#1.创建全局套接字
# udpsocket = socket(AF_INET,SOCK_DGRAM)

#接收函数
def revc():
    # global udpsocket
    while True:
        revcData = udpsocket.recvfrom(1024)
        time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("\r>>[%s]%s:%s"%(time,revcData[1],revcData[0].decode('gb2312')))
        print("<<")

def send():
    # global udpsocket
    sendArr = ('192.168.65.1', 8080)
    while True:
        sendData = str(input("<<"))
        udpsocket.sendto(sendData.encode('gb2312'),sendArr)


def main():
    #下面更改了全局变量，所以要声明
    global udpsocket
    #在外面声明udpsocket并在这个创建套接字比在外面创建套接字好
    udpsocket = socket(AF_INET, SOCK_DGRAM)

    #2.绑定地址
    Addr = udpsocket.bind(('',7890))

    #3.创建线程
    t1 = Thread(target=revc)
    t2 = Thread(target=send)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()