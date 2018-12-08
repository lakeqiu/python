from socket import *
import time

udpsocket = socket(AF_INET,SOCK_DGRAM)

#绑定端口
udpsocket.bind(("",7788))

while True:
    #接受数据
    revcDate = udpsocket.recvfrom(1024)

    #解包,content表示内容，destIfno表示发送方地址
    content,destIfno = revcDate

    print("未解包的：",end='')
    print(revcDate)
    print("未解码的：%s"%content)
    print("解包和解码的：%s"%content.decode("gb2312"))

    time.sleep(1)