from socket import *


#1.创建套接字
udpSocket = socket(AF_INET,SOCK_DGRAM)

#2.准备接受方地址
sendArr = ('192.168.65.1',8080)

#3.从键盘上获取数据
sendDate = input("请输入：")


#4.发送到指定电脑
udpSocket.sendto(sendDate.encode("gb2312"),sendArr)  #将编码转为gb2312格式

#5.关闭套接字
udpSocket.close()



# from socket import *
# #1. 创建套接字
# udpSocket = socket(AF_INET, SOCK_DGRAM)
# #2. 准备接收方的地址
# sendAddr = ('192.168.65.1', 8080)
# #3. 从键盘获取数据
# sendData = input("请输入要发送的数据:")
# #4. 发送数据到指定的电脑上
# udpSocket.sendto(sendData,sendAddr)
# #5. 等待接收对方发送的数据
# recvData = udpSocket.recvfrom(1024) # 1024表示本次接收的最大字节数
# #6. 显示对方发送的数据
# print(recvData)
# #7. 关闭套接字
# udpSocket.close()