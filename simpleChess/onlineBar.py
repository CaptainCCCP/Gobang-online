import socket
import tkinter
from tkinter import *
import tkinter.messagebox
import numpy as np
import threading
from threading import Thread
def callbackone():
    global signals, clientSocketObj, startyet
    while signals==1:
        data = clientSocketObj.recv(1024)
        data = data.decode()
        print(f"白方说：{data}")
        if "," in data:
            i, j = data.split(",")
            i = int(i)
            j = int(j)
            w1.create_oval(40 * i + 5, 40 * j + 5, 40 * i + 35, 40 * j + 35, fill='white', tags='last')
            A[i][j] = 1
            t = "w"
            B[i][j] = t
            startyet = 0
            winlose(i, j, pvproot, B)
            pvproot.update()
        else:
            print('quit?')
            quit()

def callbacktwo():
    global signals, client, startyet
    while signals == 0:
        data = client.recv(1024)
        data = data.decode()
        print(f"黑方说：{data}")
        if "," in data:
            i, j = data.split(",")
            i = int(i)
            j = int(j)
            w1.create_oval(40 * i + 5, 40 * j + 5, 40 * i + 35, 40 * j + 35, fill='black', tags='last')
            A[i][j] = 1
            t = "b"
            B[i][j] = t
            startyet = 0
            winlose(i, j, pvproot, B)
            pvproot.update()
        else:
            print('quit?client')
            quit()


# def hui(self):
#     if len(self.order) == 0:
#         return
#
#     self.board.canvas.delete("last")
#     z = self.order.pop()
#     x = z % 15
#     y = z // 15
#     self.db[y][x] = 2  # 标记为空
#     self.color_count = 1
#     for i in self.order:
#         ix = i % 15
#         iy = i // 15
#         self.change_color()
#         self.board.canvas.create_oval(40 * i + 5, 40 * j + 5, 40 * i + 35, 40 * j + 35, fill=self.color, tags='last')
#     self.change_color()
#     self.game_print.set("请" + self.color + "落子")


def createGame():
    global clientSocketObj, server

    ip = entry1.get()
    duankou = entry2.get()

    server = socket.socket()
    server.bind((ip, int(duankou)))
    server.listen(3)
    tkinter.messagebox.showinfo("提示", "等待连接中...")

    clientSocketObj, addr = server.accept()
    tkinter.messagebox.showinfo("提示", "连接成功！")

    # clientSocketObj是新的socket对象，服务器通过其与客户端通信
    # addr是客户的internet地址
    print("连接成功：客户端地址: %s" % str(addr))

    createboard(1)
    onlineroot.destroy()


def joinGame():
    global client

    ip = entry1.get()
    duankou = entry2.get()
    client = socket.socket()
    client.connect((ip, int(duankou)))
    tkinter.messagebox.showinfo("提示", "连接成功！")
    onlineroot.destroy()
    createboard(0)

    onlineroot.destroy()


def winlose(i, j, pvproot, B):
    # i,j 为新的棋子的坐标     pvproot为游戏窗口   B为全null array
    # f代表横竖左右斜共四个方向
    f = [[-1, 0], [-1, 1], [0, 1], [1, 1]]  # 用来加在x y上
    for z in range(0, 4):
        a, b = f[z][0], f[z][1]   # 例 [-1, 0] a和b分别为前后两个数
        count1, count2 = 0, 0     # 重新计数
        x, y = i, j   # 将检查的坐标重新拿回起点（即新下的这颗棋子）

        while B[x][y][0] == B[i][j][0]:  # while同颜色
            count1 += 1
            if x + a >= 0 and y + b >= 0 and x + a < 15 and y + b < 15 and B[x + a][y + b][0] == B[i][j][0]:
                # 下一个位置未出界并且颜色相等
                [x, y] = np.array([x, y]) + np.array([a, b])
                # 继续动下去
            else:
                x, y = i, j
                break
                # 回起点重新开始

        while B[x][y][0] == B[i][j][0]:
            # 从起点出发与count1相反的方向
            count2 += 1
            if x - a < 15 and y - b < 15 and x - a >= 0 and y - b >= 0 and B[x - a][y - b][0] == B[i][j][0]:
                [x, y] = np.array([x, y]) - np.array([a, b])
            else:
                break

        if count1 + count2 == 6:
            if B[i][j][0] == "b":
                tkinter.messagebox.showinfo('提示', '黑棋获胜')
                pvproot.destroy()
            else:
                tkinter.messagebox.showinfo('提示', '白棋获胜')
                pvproot.destroy()


def callback1(event):
    global num, signals, i, j, sent,clientSocketObj
    # signals用于区分状态0b 1w -1none   i, j为鼠标位置   num为棋子序号   sent为发送的信息
    if signals != 0:
        return
    else:
        for j in range(0, 15):
            for i in range(0, 15):
                if (event.x - 20 - 40 * i) ** 2 + (event.y - 20 - 40 * j) ** 2 <= 2 * 20 ** 2:
                    break
            if (event.x - 20 - 40 * i) ** 2 + (event.y - 20 - 40 * j) ** 2 <= 2 * 20 ** 2:
                break
        print('按了')
        signals = 1
        if A[i][j] != 1:  # 如果这个位置没棋子
            w1.create_oval(40 * i + 5, 40 * j + 5, 40 * i + 35, 40 * j + 35, fill='black', tags='last')
            order.append((i, j, 0))


            A[i][j] = 1
            t = "b"
            B[i][j] = t
            send_data = str(i) + "," + str(j)
            clientSocketObj.send(send_data.encode())

            winlose(i, j, pvproot, B)
            sent.set("现在轮到白方落子")

            pvproot.update()


def callback2(event):
    global signals, i, j, sent, client, startyet
    if signals != 1:
        return
    else:
        for j in range(0, 15):
            for i in range(0, 15):
                if (event.x - 20 - 40 * i) ** 2 + (event.y - 20 - 40 * j) ** 2 <= 2 * 20 ** 2:
                    break
            if (event.x - 20 - 40 * i) ** 2 + (event.y - 20 - 40 * j) ** 2 <= 2 * 20 ** 2:
                break
        print('按了')
        signals = 0
        if A[i][j] != 1:
            # signals = -1
            w1.create_oval(40 * i + 5, 40 * j + 5, 40 * i + 35, 40 * j + 35, fill='white', tags='last')
            order.append((i, j, 1))

            A[i][j] = 1
            t = "w"
            B[i][j] = t
            winlose(i, j, pvproot, B)
            send_data = str(i) + "," + str(j)
            client.send(send_data.encode())
            sent.set("现在轮到黑方落子")

            pvproot.update()

def start():
    global startyet
    startyet = 1

def quit():
    global clientSocketObj
    senddata = "quit"
    try:
        clientSocketObj.send(senddata.encode())
        clientSocketObj.close()
        server.close()
    except:
        client.send(senddata.encode())
        client.close()
    pvproot.destroy()


def createboard(info):
    global startyet, signals, pvproot, A, B, w1, sent , order
    # sent用来发送信息并显示    pvproot为窗口    w1为canvas    info区分黑白
    # A为全0array    B为全null array
    startyet = 0
    signals = 0  # 黑方先行
    order = []
    sent = StringVar()
    sent.set("现在轮到黑方落子")

    A = np.full((15, 15), 0)
    B = np.full((15, 15), "null")

    pvproot = Tk()  # 创建窗口
    pvproot.title("欢乐五子棋")

    l3 = Label(pvproot, textvariable=sent, font=('楷体', 15))
    l3.pack()

    w1 = Canvas(pvproot, width=600, height=600, background='navajowhite')
    w1.pack()
# 绘制棋盘
    for i in range(0, 15):
        w1.create_line(i * 40 + 20, 20, i * 40 + 20, 580)
        w1.create_line(20, i * 40 + 20, 580, i * 40 + 20)
    w1.create_oval(135, 135, 145, 145, fill='black')
    w1.create_oval(135, 455, 145, 465, fill='black')
    w1.create_oval(465, 135, 455, 145, fill='black')
    w1.create_oval(455, 455, 465, 465, fill='black')
    w1.create_oval(295, 295, 305, 305, fill='black')
# 一些提示
    if info == 1:
        tkinter.messagebox.showinfo("提示", "你是黑方，先下")
        w1.bind("<Button -1>", callback1)

        startbtn = Button(pvproot, text="开始游戏", width=10, height=1, command=start, font=('楷体', 15), bg="Floralwhite")
        startbtn.pack()
        u = Button(pvproot, text="退出游戏", width=10, height=1, command=quit, font=('楷体', 15), bg="Floralwhite")
        u.pack(fill=X)

        tb = Thread(target=callbackone())
        tb.start()

        pvproot.mainloop()
    else:
        tkinter.messagebox.showinfo("提示", "你是白方，请单击鼠标并等待黑方开局")
        w1.bind("<Button -1>", callback2)

        startbtn = Button(pvproot, text="开始游戏", width=10, height=1, command=start, font=('楷体', 15), bg="Floralwhite")
        startbtn.pack()
        u = Button(pvproot, text="退出游戏", width=10, height=1, command=quit, font=('楷体', 15), bg="Floralwhite")
        u.pack(fill=X)

        tw = Thread(target=callbacktwo())
        tw.start()

        pvproot.mainloop()



def onlinewindow():
    global entry1, onlineroot, entry2
    onlineroot = Tk()

    l1 = Label(onlineroot, text="ip")
    l1.grid(row=0, column=0)
    l1 = Label(onlineroot, text="port")
    l1.grid(row=1, column=0)

    entry1 = Entry(onlineroot, font=('黑体', 12))
    entry1.insert(0, "127.0.0.1")
    entry1.grid(row=0, column=1)

    entry2 = Entry(onlineroot, font=('黑体', 12))
    entry2.insert(0, "9999")
    entry2.grid(row=1, column=1)

    createButton = Button(onlineroot, command=createGame, text="创建游戏", bd="5", width=28)
    joinButton = Button(onlineroot, command=joinGame, text="加入游戏", bd="5", width=28)
    createButton.grid(row=2, column=0, columnspan=2, )
    joinButton.grid(row=3, column=0, columnspan=2)

    onlineroot.mainloop()
