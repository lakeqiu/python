from socket import *


#1.创建套接字
clientsocket = socket(AF_INET,SOCK_STREAM)

#2.连接服务器,发送过去的数据都是元组
Addr = ("192.168.65.1",8080)
clientsocket.connect(Addr)

#3.给服务器发送数据，sendData。encode()可以解决报错问题
sendData = input("请输入：")
clientsocket.send(sendData.encode('gb2312'))

#4.等待服务器返回数据（3,4不一定要一起执行，这个过程就像打电话，连通后想做什么就做什么）
revcData = clientsocket.recv(1024)
print(str(revcData.decode('gb2312')))

#5.关闭套接字
clientsocket.close()