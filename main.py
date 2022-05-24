import tkinter as tk
from tkinter import Tk, Frame, Button, Label
import time
import Mod1_Block1
import Mod1_Block2
import Mod1_Block3
import Mod2_Block1
import Mod2_Block2
import Mod2_Block3
from util import text2, text3, bg_main, fnt, btn2


def main():

    root = Tk()
    root.title("Education module")
    root.geometry("700x300+50+50")
    root.minsize(700, 300)
    root.config(bg=bg_main)

    block1 = Frame(root, bg=bg_main)
    block1.pack(side=tk.TOP, fill=tk.X, ipadx=10, ipady=10, expand=1)
    lb_t = Label(block1, text="Обучающий модуль",
                 bg=bg_main, fg=text2, font=("consolas", 18))
    lb_t.pack(side=tk.TOP, padx=10, pady=10)
    # time
    localtime = time.asctime(time.localtime(time.time()))
    lb_time = Label(block1, text=localtime,
                    bg=bg_main, fg=text2, font=fnt)
    lb_time.pack(side=tk.TOP)

    block2 = Frame(root, bg=bg_main)
    block2.pack(side=tk.BOTTOM, fill=tk.BOTH, ipadx=10, ipady=10, expand=1)

    block_left = Frame(block2, bg=bg_main)
    block_left.pack(side=tk.LEFT, fill=tk.BOTH, ipadx=10, ipady=10, expand=1)
    lb_l = Label(block_left, text="ЭЦП Эль-Гамаля",
                 bg=bg_main, fg=text2, font=("consolas", 14))
    lb_l.pack()
    bt_l_1 = Button(block_left, text="Генерация ключей", command=Mod1_Block1.click_bt_l_1,
                    bg=btn2, fg=text3, font=fnt, relief=tk.RIDGE)
    bt_l_1.pack(side=tk.TOP, padx=10, pady=10)
    bt_l_2 = Button(block_left, text="Создание подписи", command=Mod1_Block2.click_bt_l_2,
                    bg=btn2, fg=text3, font=fnt, relief=tk.RIDGE)
    bt_l_2.pack(side=tk.TOP, padx=10, pady=10)
    bt_l_3 = Button(block_left, text="Проверка подписи", command=Mod1_Block3.click_bt_l_3,
                    bg=btn2, fg=text3, font=fnt, relief=tk.RIDGE)
    bt_l_3.pack(side=tk.TOP, padx=10, pady=10)

    block_right = Frame(block2, bg=bg_main)
    block_right.pack(side=tk.RIGHT, fill=tk.BOTH, ipadx=10, ipady=10, expand=1)
    lb_r = Label(block_right, text="Задача дискретного логарифмирования",
                 bg=bg_main, fg=text2, font=("consolas", 14))
    lb_r.pack()
    bt_r_1 = Button(block_right, text="Метод согласования", command=Mod2_Block1.click_bt_r_1,
                    bg=btn2, fg=text3, font=fnt, relief=tk.RIDGE)
    bt_r_1.pack(side=tk.TOP, padx=10, pady=10)
    bt_r_2 = Button(block_right, text="Метод Сильвестра-Полига-Хеллмана",
                    command=Mod2_Block2.click_bt_r_2, bg=btn2, fg=text3, font=fnt, relief=tk.RIDGE)
    bt_r_2.pack(side=tk.TOP, padx=10, pady=10)
    bt_r_2 = Button(block_right, text="Время выполнения",
                    command=Mod2_Block3.click_bt_r_3, bg=btn2, fg=text3, font=fnt, relief=tk.RIDGE)
    bt_r_2.pack(side=tk.TOP, padx=10, pady=10)

    root.mainloop()


if __name__ == '__main__':
    main()
