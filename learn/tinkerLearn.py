from tkinter import *


def pressOk():
    print("button is press")

def pressCancle():
    print("button is released")

def quit():
    root.destroy()



if __name__ == "__main__":
    # mymainwindow()
    root = Tk()  # window
    root.title('标题')

    button1 = Button(root, text="打开", fg="black", command=pressOk)
    button1.pack()  # 布局

    quitbtn = Button(root, text="退出", fg="black", command=quit)
    # bd	按钮边界宽度，默认两个像素
    # bg	按钮背景颜色
    # command	单击按钮时，触发的函数
    # cursor	当鼠标光标移到按钮上时，按钮的形状
    # font	设置text文本的字形
    # height	按钮的高度
    # width	按钮的宽度
    # highlightbackground	当鼠标移到按钮上时的背景颜色
    # highlightcolor	当按钮取得焦点时的颜色
    # padx	设置按钮与文字的间隔
    # pady	设置按钮上下间距
    # state	设置按钮是否可用，默认可用，不可用时按钮变为灰色
    # text	按钮名称

    quitbtn.pack()  # 布局

    root.mainloop()  # loop 让窗口保持运行