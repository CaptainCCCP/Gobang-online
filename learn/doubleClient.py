from socket import *
from threading import Thread


def recv_data():
    while True:
        # 接收服务器端数据
        recv_data = client_socket.recv(1024)  # 最大接收1024字节
        recv_content = recv_data.decode('gbk')
        print(f"服务器端说:{recv_content}")
        if recv_content == "end":
            print("结束接收消息")
            break


def send_data():
    while True:
        # 给服务端发消息
        msg = input(">")
        client_socket.send(msg.encode("gbk"))
        if msg == "end":
            break


if __name__ == '__main__':
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 8899))

    t1 = Thread(target=recv_data)
    t2 = Thread(target=send_data)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    client_socket.close()