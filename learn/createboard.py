from tkinter import *
import tkinter.messagebox
import numpy as np
import datetime


class PVP:
    def resetboard(self):
        self.flag = True
        self.num = 0
        self.A = np.full((15, 15), 0)
        self.B = np.full((15, 15), "null")

    def __init__(self):
        self.resetboard()

    def createboard(self):
        while (self.flag):
            self.root = Tk()  # 创建窗口
            self.root.title("欢乐五子棋")  # 窗口名字

            self.w1 = Canvas(self.root, width=600, height=600, background='navajowhite')
            self.w1.pack()
            for i in range(0, 15):
                self.w1.create_line(i * 40 + 20, 20, i * 40 + 20, 580)
                self.w1.create_line(20, i * 40 + 20, 580, i * 40 + 20)
            self.w1.create_oval(135, 135, 145, 145, fill='black')
            self.w1.create_oval(135, 455, 145, 465, fill='black')
            self.w1.create_oval(465, 135, 455, 145, fill='black')
            self.w1.create_oval(455, 455, 465, 465, fill='black')
            self.w1.create_oval(295, 295, 305, 305, fill='black')
            self.w1.bind("<Button -1>", self.callback)
            u = Button(self.root, text="退出游戏", width=10, height=1, command=self.quit, font=('楷体', 15), bg="Floralwhite")
            u.pack(fill=X)
            mainloop()

    def callback(self, event):
        for j in range(0, 15):
            for i in range(0, 15):
                if (event.x - 20 - 40 * i) ** 2 + (event.y - 20 - 40 * j) ** 2 <= 2 * 20 ** 2:
                    break
            if (event.x - 20 - 40 * i) ** 2 + (event.y - 20 - 40 * j) ** 2 <= 2 * 20 ** 2:
                break
        if self.num % 2 == 0 and self.A[i][j] != 1:
            self.w1.create_oval(40 * i + 5, 40 * j + 5, 40 * i + 35, 40 * j + 35, fill='black')
            self.w1.create_text(40 * i + 20, 40 * j + 20, text=self.num, fill='white')
            self.A[i][j] = 1
            t = "b" + str(self.num)
            self.B[i][j] = t
            self.num += 1
        if self.num % 2 != 0 and self.A[i][j] != 1:
            self.w1.create_oval(40 * i + 5, 40 * j + 5, 40 * i + 35, 40 * j + 35, fill='white')
            self.w1.create_text(40 * i + 20, 40 * j + 20, text=self.num, fill='black')
            self.A[i][j] = 1
            t = "w" + str(self.num)
            self.B[i][j] = t
            self.num += 1

        f = [[-1, 0], [-1, 1], [0, 1], [1, 1]]
        for z in range(0, 4):
            a, b = f[z][0], f[z][1]
            count1, count2 = 0, 0
            x, y = i, j
            while self.B[x][y][0] == self.B[i][j][0]:
                count1 += 1
                if x + a >= 0 and y + b >= 0 and x + a < 15 and y + b < 15 and self.B[x + a][y + b][0] == self.B[i][j][
                    0]:
                    [x, y] = np.array([x, y]) + np.array([a, b])
                else:
                    x, y = i, j
                    break
            while self.B[x][y][0] == self.B[i][j][0]:
                count2 += 1
                if x - a < 15 and y - b < 15 and x - a >= 0 and y - b >= 0 and self.B[x - a][y - b][0] == self.B[i][j][
                    0]:
                    [x, y] = np.array([x, y]) - np.array([a, b])
                else:
                    break
            if count1 + count2 == 6:
                C = self.B.tolist()
                d = datetime.datetime.now()
                if self.B[i][j][0] == "b":
                    with open("./Record/{data}.txt".format(data=d.strftime("%Y-%m-%d-%H-%M-%S")), "w") as txt:
                        txt.write("黑胜\n")
                        for items in C:
                            for item in items:
                                txt.write(item + " ")
                            txt.write("\n")
                    self.resetboard()
                    self.flag = tkinter.messagebox.askyesno('提示', '黑棋获胜,是否重新游戏？')
                    self.root.destroy()
                else:
                    with open("./Record/{data}.txt".format(data=d.strftime("%Y-%m-%d-%H-%M-%S")), "w") as txt:
                        txt.write("白胜\n")
                        for items in C:
                            for item in items:
                                txt.write(item + " ")
                            txt.write("\n")
                    self.resetboard()
                    self.flag = tkinter.messagebox.askyesno('提示', '白棋获胜,是否重新游戏？')
                    self.root.destroy()

    def quit(self):
        self.root.destroy()
        self.flag = False


if __name__ == "__main__":
    pass