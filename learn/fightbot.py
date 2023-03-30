from learn import bot
import tkinter.messagebox
from tkinter import *
import numpy as np
from PIL import Image, ImageTk
import datetime

zuobi = False


def hack():
    global zuobi
    zuobi = True
    hackroot = Toplevel()
    hackroot.title("gua!")
    img = Image.open("1.png")
    size = 200, 200
    img.thumbnail(size)
    img_png = ImageTk.PhotoImage(img)
    label_img = Label(hackroot, image=img_png)
    label_img.pack()
    u = Button(hackroot, text="确定", width=10, height=1, command=hackroot.destroy, font=('楷体', 15), bg="Floralwhite")
    u.pack(fill=X)
    hackroot.mainloop()


def callback(event):
    global num
    for j in range(0, 15):
        for i in range(0, 15):
            if (event.x - 20 - 40 * i) ** 2 + (event.y - 20 - 40 * j) ** 2 <= 2 * 20 ** 2:
                break
        if (event.x - 20 - 40 * i) ** 2 + (event.y - 20 - 40 * j) ** 2 <= 2 * 20 ** 2:
            break
    if A[i][j] == 1 and zuobi == False: return
    A[i][j] = 1
    num += 1
    B[i][j] = "b" + str(num)
    w1.create_oval(40 * i + 5, 40 * j + 5, 40 * i + 35, 40 * j + 35, fill='black')
    w1.create_text(40 * i + 20, 40 * j + 20, text=str(num), fill='white')
    chessdata[i][j] = 1
    aibot = bot.Chess(chessdata)
    point = bot.Point(i, j)
    winornot = aibot.JudgeWin_Lose(point, 1)
    if winornot != True:
        point2 = aibot.DownChess(-1)
        A[point2.x][point2.y] = 1
        num += 1
        B[point2.x][point2.y] = "w" + str(num)
        chessdata[point2.x][point2.y] = -1
        w1.create_oval(40 * point2.x + 5, 40 * point2.y + 5, 40 * point2.x + 35, 40 * point2.y + 35, fill='white')
        w1.create_text(40 * point2.x + 20, 40 * point2.y + 20, text=str(num), fill='black')
        winornot = aibot.JudgeWin_Lose(point2, -1)
        if winornot:
            tkinter.messagebox.showinfo("对局结果", "人机获胜")
            C = B.tolist()
            d = datetime.datetime.now()
            with open("./Record/{data}.txt".format(data=d.strftime("%Y-%m-%d-%H-%M-%S")), "w") as txt:
                txt.write("人机获胜\n")
                for items in C:
                    for item in items:
                        txt.write(item + " ")
                    txt.write("\n")
            botroot.destroy()
    else:
        tkinter.messagebox.showinfo("对局结果", "玩家获胜")
        C = B.tolist()
        d = datetime.datetime.now()
        with open("./Record/{data}.txt".format(data=d.strftime("%Y-%m-%d-%H-%M-%S")), "w") as txt:
            if zuobi == True:
                txt.write("玩家获胜(作弊)\n")
            else:
                txt.write("玩家获胜\n")
            for items in C:
                for item in items:
                    txt.write(item + " ")
                txt.write("\n")
        botroot.destroy()
    del aibot


def createboard():
    global w1, A, chessdata, botroot, B, num, zuobi
    zuobi = False
    A = np.full((15, 15), 0)
    B = np.full((15, 15), "null")
    num = 0
    chessdata = np.full((15, 15), 0)
    botroot = Tk()  # 创建窗口
    botroot.title("人机对战")  # 窗口名字
    w1 = Canvas(botroot, width=600, height=600, background='navajowhite')
    w1.pack()
    for i in range(0, 15):
        w1.create_line(i * 40 + 20, 20, i * 40 + 20, 580)
        w1.create_line(20, i * 40 + 20, 580, i * 40 + 20)
    w1.create_oval(135, 135, 145, 145, fill='black')
    w1.create_oval(135, 455, 145, 465, fill='black')
    w1.create_oval(465, 135, 455, 145, fill='black')
    w1.create_oval(455, 455, 465, 465, fill='black')
    w1.create_oval(295, 295, 305, 305, fill='black')
    w1.bind("<Button -1>", callback)
    u = Button(botroot, text="退出游戏", width=10, height=1, command=botroot.destroy, font=('楷体', 15), bg="Floralwhite")
    u2 = Button(botroot, text="呱！", width=10, height=1, command=hack, font=('楷体', 15), bg="Floralwhite")
    u.pack(fill=X)
    u2.pack(fill=X)
    mainloop()