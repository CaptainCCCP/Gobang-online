
class PVE:
    def pressStart(self):
        print("开始游戏")
        self.pveroot.destroy()
        game = Gobangself.Gobang()

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