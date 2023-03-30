import socket
from threading import Thread


def recv_data():
    while True:
        recv_data = client_socket.recv(1024)  # 最大接收1024字节
        recv_content = recv_data.decode("gbk")
        print(f"客户端说:{recv_content},来自:{client_info}")
        if recv_content == "end":
            print("结束接收消息！")
            break


def send_data():
    while True:
        msg = input(">")
        client_socket.send(msg.encode("gbk"))
        if msg == "end":
            print("结束发送消息！")
            break


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 建立TCP套接字
    port=9999
    host = socket.gethostname()
    server_socket.bind((host, port))  # 本机监听8899端口

    server_socket.listen(5)
    print("等待接收连接！")
    client_socket, client_info = server_socket.accept()
    print("一个客户端建立连接成功！")

    t1 = Thread(target=recv_data)
    t2 = Thread(target=send_data)
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    client_socket.close()
    server_socket.close()