import socket
from socket import socket
from tkinter import *
from PIL import Image, ImageTk


# 定义棋盘类
class chessBoard():

    def pressReturn(self):
        print("请求悔棋")

    def quit(self):
        self.window.destroy()

    def __init__(self):
        self.window = Tk()
        self.window.title("五子棋游戏20074411")
        self.window.geometry("660x470")
        self.window.resizable()
        self.canvas = Canvas(self.window, bg="#EEE8AC", width=470, height=470)
        self.paint_board()
        self.canvas.grid(row=0, column=0)

        buttonPve = Button(self.window, text="单人游戏", fg="black", command=self.pressReturn)
        buttonPve.pack()  # 布局

        buttonQuit = Button(self.window, text="退出游戏", fg="black", command=quit)
        buttonQuit.pack()  # 布局

    def paint_board(self):
        for row in range(0, 15):
            # 横线
            if row == 0 or row == 14:
                self.canvas.create_line(25, 25 + row * 30, 25 + 14 * 30, 25 + row * 30, width=2)
            else:
                self.canvas.create_line(25, 25 + row * 30, 25 + 14 * 30, 25 + row * 30, width=1)
        for column in range(0, 15):
            # 竖线
            if column == 0 or column == 14:
                self.canvas.create_line(25 + column * 30, 25, 25 + column * 30, 25 + 14 * 30, width=2)
            else:
                self.canvas.create_line(25 + column * 30, 25, 25 + column * 30, 25 + 14 * 30, width=1)
        # 小点
        self.canvas.create_oval(112, 112, 118, 118, fill="black")
        self.canvas.create_oval(352, 112, 358, 118, fill="black")
        self.canvas.create_oval(112, 352, 118, 358, fill="black")
        self.canvas.create_oval(232, 232, 238, 238, fill="black")
        self.canvas.create_oval(352, 352, 358, 358, fill="black")


class PVE:
    def pressStart(self):
        print("开始游戏")
        self.pveroot.destroy()
        board = chessBoard()


    def quit(self):
        self.pveroot.destroy()

    def __init__(self):
        self.pveroot = Tk()  # window
        self.pveroot.title('20074411郭尚仪')
        buttonPvp = Button(self.pveroot, text="开始游戏", fg="black", command=self.pressStart)
        buttonPvp.pack()  # 布局

        buttonQuit = Button(self.pveroot, text="退出游戏", fg="black", command=quit)
        buttonQuit.pack()  # 布局

        self.pveroot.mainloop()  # loop 让窗口保持运行


# 进入游戏后的主页面
class Openning:
    def pressPvp(self):
        print("内网对战")

    def pressPve(self):
        print("单人游戏")
        self.root.destroy()
        pve = PVE()

    def pressOnline(self):
        print("在线对战")

    def quit(self):
        self.root.destroy()

    def __init__(self):
        self.root = Tk()  # window
        self.root.title('20074411郭尚仪')
        buttonPvp = Button(self.root, text="内网对战", fg="black", command=self.pressPvp)
        buttonPvp.pack()  # 布局

        buttonPve = Button(self.root, text="单人游戏", fg="black", command=self.pressPve)
        buttonPve.pack()  # 布局

        buttonOnline = Button(self.root, text="在线对战", fg="black", command=self.pressOnline)
        buttonOnline.pack()  # 布局

        buttonQuit = Button(self.root, text="退出游戏", fg="black", command=quit)
        buttonQuit.pack()  # 布局

        self.root.mainloop()  # loop 让窗口保持运行


if __name__ == "__main__":
    start = Openning()