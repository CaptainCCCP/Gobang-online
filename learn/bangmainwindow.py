import socket
import sys

# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET internet   AF_UNIX用于同一台机器进程间通信
# 获取本地主机名
host = socket.gethostname()
port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)
print("等待接收连接！")

while True:
    # 建立客户端连接
    clientsocket, client_addr = serversocket.accept()     # clientsocket是新的socket对象，服务器通过其与客户端通信
    print("连接成功：地址: %s" % str(client_addr))                # addr是客户的internet地址


    # msg = '欢迎访问菜鸟教程！' + "\r\n"
    # clientsocket.send(msg.encode('utf-8'))

    recv_data = clientsocket.recv(1024)  # 最大接收1024字节
    recv_content = recv_data.decode('gbk')
    print(f"客户端说:{recv_content},来自:{client_addr}")
    if recv_content == "end":
        break
    msg = input(">")
    clientsocket.send(msg.encode("gbk"))

clientsocket.close()
serversocket.close()