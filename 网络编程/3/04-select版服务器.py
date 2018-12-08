from socket import *
import select
import sys

#select最多只有1024(32位系统)，2048（64）个套接字
# def main():
if __name__ == '__main__':
    #1.创建套接字
    tcpsocket = socket(AF_INET,SOCK_STREAM)

    #2.绑定地址
    tcpsocket.bind(('',8090))

    #3.变主动套接字为被动套接字
    tcpsocket.listen(5)

    #用来存放套接字
    inputs = [tcpsocket,sys.stdin]

    running = True

    while True:
        # 调用 select 函数，阻塞等待（采用轮询方式，效率低）
        readable,writeable,exceptional = select.select(inputs,[],[])

        #每个有消息套接字遍历一遍
        for x in readable:

            #为被动套接字
            if x == tcpsocket:
                newsocket,clientAddr = tcpsocket.accept()
                inputs.append(newsocket)

             # 监听到键盘有输入
            elif x == sys.stdin:
                cmd = sys.stdin.readline()
                running = False
                break


            #对客户端服务的套接字
            else:
                recvData = x.recv(1024)
                #发送过来数据不为零
                if recvData:
                    x.send(recvData)
                #发送数据为零
                else:
                    # 移除select监听的socket
                    inputs.remove(x)
                    x.close()

        # 如果检测到用户输入敲击键盘，那么就退出
        if not running:
            break

    tcpsocket.close()


# if __name__ == '__main__':
#     main()