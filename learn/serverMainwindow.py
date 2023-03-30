from tkinter import *
from PIL import Image, ImageTk


def combine1():  # 创建双人对战棋盘
    quit()
    pvp = createboard.PVP()
    pvp.createboard()
    mainwindow()
    del pvp

def combine2():  # 创建单人对战棋盘
    quit()
    fightbot.createboard()
    mainwindow()

def combine3():  # 创建战绩查询菜单
    quit()
    search.readin()
    mainwindow()

def combine4():  # 创建在线对战棋盘
    quit()
    online.onlinewindow()
    mainwindow()

def quit():
    mainroot.destroy()


def mainwindow():
    global mainroot

    img = Image.open("../src/background.jpg")
    size = 200, 200
    img.thumbnail(size)  # 绘制略缩图

    mainroot = Tk()  # tinker 窗口
    mainroot.title("五子棋20074411")

    w = Button(mainroot, activebackground="black",
            bg = "navajowhite",      #按钮背景颜色
            text = "双人对战",
            font = ("宋体", 16, "bold"),
            bd = "5",                #按钮大小
            fg = "black",
            command = combine1)
    w2 = Button(mainroot,activebackground="black",
            bg = "navajowhite",      #按钮背景颜色
            text = "人机对战",
            font = ("宋体", 16, "bold"),
            bd = "5",                #按钮大小
            fg = "black",
            command = combine2)
    w3 = Button(mainroot,activebackground="black",
            bg = "navajowhite",      #按钮背景颜色
            text = "战绩查询",
            font = ("宋体", 16, "bold"),
            bd = "5",                #按钮大小
            fg = "black",
            command = combine3)
    w4 = Button(mainroot,activebackground="black",
            bg = "navajowhite",      #按钮背景颜色
            text = "退出游戏",
            font = ("宋体", 16, "bold"),
            bd = "5",                #按钮大小
            fg = "black",
            command = quit,
            width=17)
    w5 = Button(mainroot,activebackground="black",
            bg = "navajowhite",      #按钮背景颜色
            text = "在线对战",
            font = ("宋体", 16, "bold"),
            bd = "5",                #按钮大小
            fg = "black",
            command = combine4)

    w.grid(row=0,column=0)
    w2.grid(row=0,column=1)
    w3.grid(row=1,column=0)
    w5.grid(row=1,column=1)
    w4.grid(row=6,column=0,columnspan=2)
    img_png = ImageTk.PhotoImage(img)
    label_img = Label(mainroot, image = img_png)
    label_img.grid(row=2,column=0,rowspan=4,columnspan=2)
    mainroot.mainloop()


if __name__ == "__main__":
    mainwindow()
