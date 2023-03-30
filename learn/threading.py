from tkinter import *
import socket
import os
import time
from pykeyboard import*
import threading
#初始化各种参数
def initial_parameter():
    global BOARD_LENGTH,OFFSET,LINE_INTERVAL,all_chesspoint,YOURCHESS_COLOR,RIVALCHESS_COLOR,HOST_addr,\
        CLIENT_addr,aim_coordx,aim_coordy,x,y,over,flag
    #初始化棋盘参数
    BOARD_LENGTH=560
    OFFSET=20
    LINE_INTERVAL=40
    #初始化位置状态数组
    all_chesspoint=[[0 for i in range(15)]for j in range(15)]#用来存储棋盘格上每个点是否有棋子，1白棋，-1黑棋，0没有棋子
    YOURCHESS_COLOR=-1#您是黑棋（后行）
    RIVALCHESS_COLOR=1
    x=7;y=7#光标初始位置
    aim_coordx=OFFSET+x*LINE_INTERVAL;aim_coordy=OFFSET+y*LINE_INTERVAL#位置转像素坐标转化公式
    over=1
    flag=1
#画棋盘函数
def drawmap():
    cv.create_rectangle(20, 20, 580, 580, outline='brown', width=5)
    for i in range(13):
        cv.create_line(60+40*i,20,60+40*i,580,fill='brown')
    for i in range(13):
        cv.create_line(20,60+40*i,580,60+40*i,fill='brown')
#画准心函数
def drawaim(aim_coordx,aim_coordy):
    cv.create_rectangle(aim_coordx-18,aim_coordy-18,aim_coordx+18,aim_coordy+18,outline='red')
#删除准心函数(用白色覆盖)
def deleteaim(aim_coordx,aim_coordy):
    cv.create_rectangle(aim_coordx-18,aim_coordy-18,aim_coordx+18,aim_coordy+18,outline='white')
#画一颗棋子
def drawchess(aim_coordx,aim_coordy,color):#color=1为白棋,color=-1为黑棋,其他就不画
    if color==1:
        cv.create_oval(aim_coordx-15,aim_coordy-15,aim_coordx+15,aim_coordy+15,fill='white',outline='black',width=2)
    elif color==-1:
        cv.create_oval(aim_coordx-15,aim_coordy-15,aim_coordx+15,aim_coordy+15,fill='black',outline='black',width=2)
    else:
        pass
#画全部棋子
def drawallchess():#根据当下的位置状态数组画棋子
    global OFFSET,LINE_INTERVAL,all_chesspoint
    for i in range(15):
        for j in range(15):
            drawchess(OFFSET+i*LINE_INTERVAL,OFFSET+j*LINE_INTERVAL,all_chesspoint[i][j])
def udpServer(udp_server,send_data):
    global all_chesspoint,HOST_addr,CLIENT_addr,over
    drawallchess()
    root.update_idletasks()
    udp_server.sendto(send_data.encode('utf-8'),CLIENT_addr) #发送数据
    recv_data, server_addr = udp_server.recvfrom(1024)#接受数据，等待对方反应......
    x_alter, y_alter = eval(recv_data.decode('utf-8'))
    all_chesspoint[int(x_alter)][int(y_alter)]= RIVALCHESS_COLOR#将改变后的数据在数组更新
    drawallchess()#刷新对方下完的棋盘
#响应键盘事件
def callback(event):
    global x,y,all_chesspoint,over,flag
    if over==1:#防止多次触发
        over = 0
        if event.char=='w' :
            deleteaim(OFFSET + x * LINE_INTERVAL, OFFSET + y * LINE_INTERVAL)
            if y>0:
                y=y-1
            else:
                y=14
            drawmap()
            drawaim(OFFSET + x * LINE_INTERVAL, OFFSET + y * LINE_INTERVAL)
            drawallchess()
        elif event.char=='s':
            deleteaim(OFFSET + x * LINE_INTERVAL, OFFSET + y * LINE_INTERVAL)
            if y<14:
                y=y+1
            else:
                y=0
            drawmap()
            drawaim(OFFSET + x * LINE_INTERVAL, OFFSET + y * LINE_INTERVAL)
            drawallchess()
        elif event.char=='a':
            deleteaim(OFFSET + x * LINE_INTERVAL, OFFSET + y * LINE_INTERVAL)
            if x>0:
                x=x-1
            else:
                x=14
            drawmap()
            drawaim(OFFSET + x * LINE_INTERVAL, OFFSET + y * LINE_INTERVAL)
            drawallchess()
        elif event.char=='d':
            deleteaim(OFFSET + x * LINE_INTERVAL, OFFSET + y * LINE_INTERVAL)
            if x<14:
                x=x+1
            else:
                x=0
            drawmap()
            drawaim(OFFSET + x * LINE_INTERVAL, OFFSET + y * LINE_INTERVAL)
            drawallchess()
        elif event.keycode==13:
            all_chesspoint[int(x)][int(y)]=YOURCHESS_COLOR
            print(all_chesspoint)
            udpServer(udp_server, '{},{}'.format(x,y))  # 发送并等待
        else:
            pass
        over=1
def sub_func1(root):
    recv_data, server_addr = udp_server.recvfrom(1024)  # 接受数据，等待对方反应......
    x_alter, y_alter = eval(recv_data.decode('utf-8'))
    all_chesspoint[int(x_alter)][int(y_alter)] = RIVALCHESS_COLOR  # 将改变后的数据在数组更新
    drawmap()  # 刷新空棋盘
    drawallchess()  # 刷新对方下完的棋盘
    root.update_idletasks()
    '''k = PyKeyboard()
    time.sleep(5)
    k.tap_key(k.alt_key)'''

#主程序---------------------------------------------------------------------------
aim_coordx=0;aim_coordy=0
x=0;y=0;flag=0
over=0
HOST_PORT = 8081
HOST_addr = ('', HOST_PORT)
CLIENT_IP=input("请输入对方的IP地址")
CLIENT_PORT = 8080
CLIENT_addr = (CLIENT_IP, CLIENT_PORT)
initial_parameter()
root=Tk()#创建窗口
root.title("在线五子棋v1.0  UDP_HOST [您是黑子，对方先行]")
cv=Canvas(root,bg = 'white',height=600,width=600)#创建画布
cv.pack()  # 这句很重要，没有的话无法显示
cv.focus_set()
drawmap()#创建棋盘
drawaim(aim_coordx,aim_coordy)
cv.bind(sequence='<Key>',func=callback)
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(HOST_addr)#建立连接
sub_thread=threading.Thread(target=sub_func1,args=(root,))
sub_thread.start()
root.mainloop()