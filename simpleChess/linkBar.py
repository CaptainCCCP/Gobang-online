from tkinter import *
import socket, threading


def createGame():
    threading.Thread(target=self.startListen).start()


def joinGame():
    print('la')

def startListen():
    while True:


class secondBar:
    def pressOnline(self):
        print("在线对战")

    def quit(self):
        self.secondroot.destroy()

    def __init__(self):
        self.secondroot = Tk()  # window
        self.secondroot.title('20074411郭尚仪最简五子棋')
        self.secondroot.geometry("200x200")
        self.secondroot.resizable()

        createButton = Button(self.secondroot, command=createGame, text="创建游戏", bd="5", width=28)
        joinButton = Button(self.secondroot, command=joinGame, text="加入游戏", bd="5", width=28)
        Quitbutton = Button(self.secondroot, text="退出游戏", fg="black", command=quit)

        createButton.grid(row=2, column=0, columnspan=2, )
        joinButton.grid(row=3, column=0, columnspan=2)
        Quitbutton.grid(row=4, column=0, columnspan=2)

        self.secondroot.mainloop()  # loop 让窗口保持运行


if __name__ == "__main__":
    second = secondBar()
