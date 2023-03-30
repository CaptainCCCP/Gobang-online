from tkinter import *
import os, threading, socket

# 进入游戏后的主页面
class Openning:
    def pressOnline(self):
        print("在线对战")

    def quit(self):
        self.root.destroy()

    def __init__(self):
        self.root = Tk()  # window
        self.root.title('20074411郭尚仪最简五子棋')
        self.root.geometry("200x200")
        self.root.resizable()

        buttonOnline = Button(self.root, text="在线对战", fg="black", command=self.pressOnline)
        buttonOnline.pack()  # 布局
        buttonQuit = Button(self.root, text="退出游戏", fg="black", command=quit)
        buttonQuit.pack()  # 布局

        self.root.mainloop()  # loop 让窗口保持运行


if __name__ == "__main__":
    start = Openning()
