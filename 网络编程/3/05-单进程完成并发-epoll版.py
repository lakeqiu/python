from socket import *
import select

def main():
    #1.创建套接字
    tcpsocket = socket(AF_INET,SOCK_STREAM)

    # 设置可以重复使用绑定的信息
    # tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    #2.绑定地址
    tcpsocket.bind(('', 8888))

    #3.改为被动套接字
    tcpsocket.listen(6)

    #4.创建epoll对象
    epoll = select.epoll()

    #5.注册对象到epoll中
    # 将创建的套接字添加到epoll的事件监听中
    epoll.register(tcpsocket.fileno(),select.EPOLLIN|select.EPOLLET)

    #用来存放对客户端服务的套接字
    connections = {}
    addresses = {}

    while True:

        #epoll 进行 fd 扫描的地方 -- 未指定超时时间则为阻塞等待
        #返回有事件发生的套接字文件描述符及是什么事件
        epoll_list = epoll.poll()

        #对事件进行判断
        for fd,events in epoll_list:
            # 如果是socket创建的套接字被激活
            if fd == tcpsocket.fileno():
                conn,addr = tcpsocket.accept()

                # 将 conn 和 addr 信息分别保存起来
                connections[conn.fileno()] = conn
                addresses[conn.fileno()] = addr

                # 向 epoll 中注册 连接 socket 的 可读 事件
                epoll.register(conn.fileno(),select.EPOLLIN|select.EPOLLET)


            elif events == select.EPOLLIN:
                # 从激活 fd 上接收
                recvData = connections[fd].recv(1024)

                if len(recvData) > 0:
                    print('recv:%s' % recvData)

                else:
                    #从epoll中移除该链接fd
                    epoll.unregister(fd)

                    #关闭该套接字
                    connections[fd].close()

                    print("%s---offline---" % str(addresses[fd]))

if __name__ == '__main__':
    main()