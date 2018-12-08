from socket import *
import os
import struct

#1.获取要下载的文件名
# downloadFileName = input("请输入要下载的文件名:")

#2.创建发送请求
udpsocket = socket(AF_INET,SOCK_DGRAM)
requesFiles = struct.pack('!H8sb5sb',1,b'test.png',0,b'octet',0)

num = 0
flag = True#表示能够下载数据，即不擅长，如果是false那么就删除

f = open('test.png','w')

# Addr = udpsocket.bind(('',8990))
#3.发送请求
udpsocket.sendto(requesFiles,('192.168.65.1',69))

while True:
    #4.接收服务器发回的应答数据
    responsData = udpsocket.recvfrom(1024)

    #5.拆包
    revcData,serverInfo = responsData

    #操作码
    opNum = struct.unpack("!H",revcData[0:2])

    #块编码
    packNum = struct.unpack("!H",revcData[2:4])

    #6.判断是否为下载码
    if opNum[0] == 3:           ##因为opNum此时是一个元组(3,)，所以需要使用下标来提取某个数据

        num += 1

        # 如果一个下载的文件特别大，即接收到的数据包编号超过了2个字节的大小
        # 那么会从0继续开始，所以这里需要判断，如果超过了65535 那么就改为0
        if num == 65536:
            num = 0

        #判断这次收到的包是否为上一次收到的包的下一个，如果不是则不能写入
        if packNum[0] == num:
            f.write(str(revcData[4:0]))
            num = packNum[0]

        #7.成功接收到包并写入后整理ACK数据包并发送回去
        ackData = struct.pack("!HH",4,packNum[0])
        udpsocket.sendto(ackData,serverInfo)

    elif opNum[0] == 5:
        print("没有这个文件！")
        flag = False

    if len(revcData) < 516:
        break

if flag == True:
    f.close()
else:
    os.unlink('test.png')#如果没有要下载的文件，那么就需要把刚刚创建的文件进行删除