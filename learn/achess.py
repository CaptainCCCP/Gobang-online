# @date   2020-05-11 19:56

from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox


class Chess:
    @staticmethod
    def center(window, w, h):  # 设置窗口大小且居中
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}".format(w, h, x, y))

    def is_win(self):
        for i, j in self.seq_list:
            color = self.matrix_flag[i][j]
            if j <= 10:
                for col in range(j + 1, j + 5):  # 判断横向
                    if self.matrix_flag[i][col] != color:
                        break
                else:
                    tkinter.messagebox.showinfo("提示", "黑棋你赢了！" if color == 1 else "白棋你赢了！")
                    return
            if i <= 10:
                for row in range(i + 1, i + 5):  # 判断纵向
                    if self.matrix_flag[row][j] != color:
                        break
                else:
                    tkinter.messagebox.showinfo("提示", "黑棋你赢了！" if color == 1 else "白棋你赢了！")
                    return

            if i <= 10 and j <= 10:
                for row, col in zip([x for x in range(i + 1, i + 5)], [y for y in range(j + 1, j + 5)]):  # 对角线判断
                    if self.matrix_flag[row][col] != color:
                        break
                else:
                    tkinter.messagebox.showinfo("提示", "黑棋你赢了！" if color == 1 else "白棋你赢了！")
                    return

    def undo(self, event):  # 悔棋
        if self.seq_list:
            i, j = self.seq_list.pop()
            self.canvas.delete(self.matrix_img[i][j])
            self.matrix_img[i][j] = None
            self.matrix_flag[i][j] = 0
        else:
            tkinter.messagebox.showwarning("警告", "已经没有任何棋子了！")

    def callback(self, event):  # 落子
        x, y = event.x - 20, event.y - 20
        res_x, res_y = x // 40, y // 40
        div_x, div_y = x % 40, y % 40
        flag_x = flag_y = False  # 分布判断 x , y的坐标是否在交点周围
        i = j = 0
        if div_x <= 10:
            flag_x = True
            x = res_x * 40
            j = res_x
        elif 30 <= div_x:
            flag_x = True
            x = (res_x + 1) * 40
            j = res_x + 1
        if div_y <= 10:
            flag_y = True
            y = res_y * 40
            i = res_y
        elif 30 <= div_y:
            flag_y = True
            y = (res_y + 1) * 40
            i = res_y + 1

        if flag_x and flag_y and not self.matrix_flag[i][j]:
            self.matrix_img[i][j] = self.canvas.create_image(x + 20, y + 20, image=self.img_black)
            self.img_black, self.img_white = self.img_white, self.img_black  # 黑白子交换
            self.matrix_flag[i][j] = self.count % 2 + 1  # 黑子为 1 白子为 2
            self.count += 1
            self.seq_list.append((i, j))
            self.is_win()  # 判断是否达到五个

    def __init__(self):
        self.row, self.column = 15, 15
        self.matrix_flag = [[0 for _ in range(self.row)] for _ in range(self.column)]
        self.matrix_img = [[None for _ in range(self.row)] for _ in range(self.column)]
        self.count = 0
        self.seq_list = []
        self.root = Tk()
        self.root.resizable(width=False, height=False)  # 设置窗口不可缩放
        self.root.title("五子棋")
        self.center(self.root, 600, 600)
        self.canvas = Canvas(self.root, bg="green", bd=0)
        self.canvas.pack(fill='both', expand='YES')
        self.img_black = ImageTk.PhotoImage(Image.open("blackstone.gif"))  # 加载黑棋
        self.img_white = ImageTk.PhotoImage(Image.open("whitestone.gif"))  # 加载白棋
        self.draw_grid()

        self.canvas.bind("<Button-1>", self.callback)  # 落子
        self.canvas.bind("<Button-3>", self.undo)  # 悔棋

        self.root.mainloop()

    def draw_grid(self):  # 绘制网格
        start = [(20, i) for i in range(20, 580, 40)] + [(i, 20) for i in range(20, 580, 40)] + [(20, 580), (580, 20)]
        end = [(580, i) for i in range(20, 580, 40)] + [(i, 580) for i in range(20, 580, 40)] + [(580, 580), (580, 580)]
        for i in range(len(start)):
            self.canvas.create_line((start[i], end[i]), width=2)


if __name__ == '__main__':
    Chess()
