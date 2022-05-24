import tkinter as tk
from tkinter import Tk, Frame, Label, Button, scrolledtext, Entry, Text
from random import randint
import My_ElGamal as elg
import sympy as sym
from util import text1, text2, text3, bg_main, bg_entry, btn, fnt
from util import read_text, get_prime_numbers_in_range


def click_bt_l_1():

    global win_l_1
    win_l_1 = Tk()
    win_l_1.title("ElGamal signature scheme: Keys Generation")
    win_l_1.geometry("1600x550")
    win_l_1.minsize(1400, 550)
    win_l_1.config(bg=bg_main)

    def clear(event):
        caller = event.widget
        caller.delete("0", "end")

    def example_p():
        try:
            output_ex_p.configure(state=tk.NORMAL)
            output_ex_p.delete("0.0", "end")
            a_val = int(a.get())
            b_val = int(b.get())
            if (a_val >= b_val or a_val < 0 or b_val <
                    0 or a_val >= 99000 or b_val >= 99000):
                output_ex_p.insert("0.0", "Число некорректно.")
            else:
                output_ex_p.insert(
                    "0.0", get_prime_numbers_in_range(a_val, b_val))
                output_ex_p.configure(state=tk.DISABLED)
        except ValueError:
            output_ex_p.delete("0.0", "end")
            output_ex_p.insert("0.0", "Введите два числа.")
            output_ex_p.configure(state=tk.DISABLED)

    def task_p():
        try:
            output_task_p.configure(state=tk.NORMAL)
            output_task_p.delete("0.0", "end")
            p_ent_val = int(p_ent.get())
            if (sym.isprime(p_ent_val)):
                output_task_p.insert("0.0", "Верно.")
            else:
                output_task_p.insert("0.0", "Неверно.")
            output_task_p.configure(state=tk.DISABLED)
        except ValueError:
            output_task_p.delete("0.0", "end")
            output_task_p.insert("0.0", "Введите число.")
            output_task_p.configure(state=tk.DISABLED)

    def example_g():
        try:
            output_ex_g.configure(state=tk.NORMAL)
            output_ex_g.delete("0.0", "end")
            p2_val = int(p2.get())
            if (p2_val < 0 or p2_val > 99000):
                output_ex_g.insert("0.0", "Число некорректно.")
            else:
                output_ex_g.insert("0.0", elg.get_primitive_root(p2_val))
            output_ex_g.configure(state=tk.DISABLED)
        except ValueError:
            output_ex_g.delete("0.0", "end")
            output_ex_g.insert("0.0", "Введите число.")
            output_ex_g.configure(state=tk.DISABLED)

    def task_g():
        try:
            output_task_g.configure(state=tk.NORMAL)
            output_task_g.delete("0.0", "end")
            g2_val = int(g2.get())
            if (g2_val in elg.get_primitive_roots(pg2)):
                output_task_g.insert("0.0", "Верно.")
            else:
                output_task_g.insert("0.0", "Неверно.")
            output_task_g.configure(state=tk.DISABLED)
        except ValueError:
            output_task_g.delete("0.0", "end")
            output_task_g.insert("0.0", "Введите число.")
            output_task_g.configure(state=tk.DISABLED)

    def example_x():
        try:
            output_ex_x.configure(state=tk.NORMAL)
            output_ex_x.delete("0.0", "end")
            p3_val = int(p3.get())
            if (p3_val < 0 or p3_val > 99000):
                output_ex_x.insert("0.0", "Число некорректно.")
            else:
                output_ex_x.insert("0.0",
                                   elg.get_prime_number_in_range(1, p3_val - 1))
            output_ex_x.configure(state=tk.DISABLED)
        except ValueError:
            output_ex_x.delete("0.0", "end")
            output_ex_x.insert("0.0", "Введите число.")
            output_ex_x.configure(state=tk.DISABLED)

    def task_x():
        try:
            output_task_x.configure(state=tk.NORMAL)
            output_task_x.delete("0.0", "end")
            ent_x_val = int(ent_x.get())
            if (ent_x_val > 0 and ent_x_val < p4 - 1):
                output_task_x.insert("0.0", "Верно.")
            else:
                output_task_x.insert("0.0", "Неверно.")
            output_task_x.configure(state=tk.DISABLED)
        except ValueError:
            output_task_x.delete("0.0", "end")
            output_task_x.insert("0.0", "Введите число.")
            output_task_x.configure(state=tk.DISABLED)

    def example_y():
        try:
            output_ex_y.configure(state=tk.NORMAL)
            ent_yg_val = int(ent_yg.get())
            ent_yx_val = int(ent_yx.get())
            ent_yp_val = int(ent_yp.get())
            output_ex_y.delete("0.0", "end")
            output_ex_y.insert(
                "0.0", elg.binary_pow(ent_yg_val, ent_yx_val, ent_yp_val))
            output_ex_y.configure(state=tk.DISABLED)
        except ValueError:
            output_ex_y.delete("0.0", "end")
            output_ex_y.insert("0.0", "Введите три числа.")
            output_ex_y.configure(state=tk.DISABLED)

    def task_y():
        try:
            output_task_y.configure(state=tk.NORMAL)
            output_task_y.delete("0.0", "end")
            ent_y_val = int(ent_y.get())
            res = elg.binary_pow(gy, xy, py)
            if (res == ent_y_val):
                output_task_y.insert("0.0", "Верно.")
            else:
                output_task_y.insert("0.0", "Неверно.")
            output_task_y.configure(state=tk.DISABLED)
        except ValueError:
            output_task_y.delete("0.0", "end")
            output_task_y.insert("0.0", "Введите число.")
            output_task_y.configure(state=tk.DISABLED)

    block11 = Frame(win_l_1, bg=bg_main)
    block11.pack(side=tk.LEFT, fill=tk.Y, ipadx=10, ipady=10, expand=1)
    scrlt = scrolledtext.ScrolledText(
        block11, bg=bg_main, fg=text1, font=fnt, relief=tk.FLAT)
    scrlt.pack(side=tk.LEFT, expand=1, fill=tk.Y)
    scrlt.insert(tk.INSERT, read_text("text_mod1_block1.txt"))
    scrlt.configure(state=tk.DISABLED)

    block12 = Frame(win_l_1, bg=bg_main)
    block12.pack(side=tk.RIGHT, fill=tk.Y, ipadx=10, ipady=10, expand=1)

    # Example p
    block_1 = Frame(block12, bg=bg_main)
    block_1.grid(row=1, column=1, ipadx=10, ipady=10)
    name1 = Label(block_1, text="Пример 1", bg=bg_main, fg=text2, font=fnt)
    name1.grid(row=0, column=0, sticky=tk.NW)

    lb1 = Label(block_1, text="p - простое на [",
                bg=bg_main, fg=text1, font=fnt)
    lb1.grid(row=1, column=0)
    a = Entry(block_1, width=6,
              bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    a.bind("<FocusIn>", clear)
    a.grid(row=1, column=1)
    lb2 = Label(block_1, text=",", bg=bg_main, fg=text1, font=fnt)
    lb2.grid(row=1, column=2)
    b = Entry(block_1, width=6,
              bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    b.bind("<FocusIn>", clear)
    b.grid(row=1, column=3)
    lb3 = Label(block_1, text="]", bg=bg_main, fg=text1, font=fnt)
    lb3.grid(row=1, column=4)
    output_ex_p = Text(block_1, width=40, heigh=2,
                       bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    output_ex_p.grid(row=2, column=0, columnspan=5, sticky=tk.NW)
    output_ex_p.configure(state=tk.DISABLED)
    but_ex_p = Button(block_1, text="Go", command=example_p,
                      bg=btn, fg=text3, font=fnt, relief=tk.RIDGE)
    but_ex_p.grid(row=0, column=4, sticky=tk.NE)

    # Task p
    block_2 = Frame(block12, bg=bg_main)
    block_2.grid(row=2, column=1, ipadx=10, ipady=10)
    name2 = Label(block_2, text="Задача 1", bg=bg_main, fg=text2, font=fnt)
    name2.grid(row=0, column=0, ipadx=10, ipady=10, sticky=tk.NW)

    p_ent = Entry(block_2, width=6,
                  bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    p_ent.grid(row=1, column=0)
    p_ent.bind("<FocusIn>", clear)
    A = randint(1000, 1100)
    B = A + 500
    lb4 = Label(block_2, text=f"- простое на [{A}, {B}]",
                bg=bg_main, fg=text1, font=fnt)
    lb4.grid(row=1, column=1)
    output_task_p = Text(block_2, width=40, heigh=2,
                         bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    output_task_p.grid(row=2, columnspan=3, sticky=tk.NW)
    output_task_p.configure(state=tk.DISABLED)
    bt_task_p = Button(block_2, text="Go", command=task_p,
                       bg=btn, fg=text3, font=fnt, relief=tk.RIDGE)
    bt_task_p.grid(row=0, column=2, sticky=tk.NE)

    # Example g
    block_3 = Frame(block12, bg=bg_main)
    block_3.grid(row=3, column=1, ipadx=10, ipady=10)
    name3 = Label(block_3, text="Пример 2", bg=bg_main, fg=text2, font=fnt)
    name3.grid(row=0, column=0, ipadx=10, ipady=10, sticky=tk.NW)
    lb5 = Label(block_3, text="g - первообразный корень ",
                bg=bg_main, fg=text1, font=fnt)
    lb5.grid(row=1, column=0)
    p2 = Entry(block_3, width=6,
               bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    p2.bind("<FocusIn>", clear)
    p2.grid(row=1, column=1)
    output_ex_g = Text(block_3, width=40, heigh=2,
                       bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    output_ex_g.grid(row=2, columnspan=3, sticky=tk.NW)
    output_ex_g.configure(state=tk.DISABLED)
    but_ex_g = Button(block_3, text="Go", command=example_g,
                      bg=btn, fg=text3, font=fnt, relief=tk.RIDGE)
    but_ex_g.grid(row=0, column=2, sticky=tk.NE)

    # Task g
    block_4 = Frame(block12, bg=bg_main)
    block_4.grid(row=4, column=1, ipadx=10, ipady=10)
    name4 = Label(block_4, text="Задача 2", bg=bg_main, fg=text2, font=fnt)
    name4.grid(row=0, column=0, ipadx=10, ipady=10, sticky=tk.NW)

    g2 = Entry(block_4, width=6,
               bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    g2.grid(row=1, column=0)
    g2.bind("<FocusIn>", clear)
    pg2 = elg.get_prime_number_in_range(20, 300)
    lb6 = Label(block_4, text=f"- первообразный корень {pg2}",
                bg=bg_main, fg=text1, font=fnt)
    lb6.grid(row=1, column=1)
    output_task_g = Text(block_4, width=40, heigh=2,
                         bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    output_task_g.grid(row=2, columnspan=5, sticky=tk.NW)
    output_task_g.configure(state=tk.DISABLED)
    bt_task_g = Button(block_4, text="Go", command=task_g,
                       bg=btn, fg=text3, font=fnt, relief=tk.RIDGE)
    bt_task_g.grid(row=0, column=4, sticky=tk.NE)

    # Example x
    block_5 = Frame(block12, bg=bg_main)
    block_5.grid(row=1, column=2, ipadx=10, ipady=10)
    name5 = Label(block_5, text="Пример 3", bg=bg_main, fg=text2, font=fnt)
    name5.grid(row=0, column=0, ipadx=10, ipady=10, sticky=tk.NW)

    lb7 = Label(block_5, text="1 < x < p - 1", bg=bg_main, fg=text1, font=fnt)
    lb7.grid(row=1, column=0)
    p3 = Entry(block_5, width=6,
               bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    p3.bind("<FocusIn>", clear)
    p3.grid(row=1, column=1)
    output_ex_x = Text(block_5, width=40, heigh=2,
                       bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    output_ex_x.grid(row=2, columnspan=6, sticky=tk.NW)
    output_ex_x.configure(state=tk.DISABLED)
    but_ex_x = Button(block_5, text="Go", command=example_x,
                      bg=btn, fg=text3, font=fnt, relief=tk.RIDGE)
    but_ex_x.grid(row=0, column=5, sticky=tk.NE)

    # Task x
    block_6 = Frame(block12, bg=bg_main)
    block_6.grid(row=2, column=2, ipadx=10, ipady=10)
    name6 = Label(block_6, text="Задача 3", bg=bg_main, fg=text2, font=fnt)
    name6.grid(row=0, column=0, ipadx=10, ipady=10, sticky=tk.NW)

    lb8 = Label(block_6, text="1 <", bg=bg_main, fg=text1, font=fnt)
    lb8.grid(row=1, column=0)
    ent_x = Entry(block_6, width=6,
                  bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_x.grid(row=1, column=1)
    ent_x.bind("<FocusIn>", clear)
    p4 = elg.get_prime_number_in_range(100, 1000)
    lb9 = Label(block_6, text=f"< {p4 - 1}", bg=bg_main, fg=text1, font=fnt)
    lb9.grid(row=1, column=2)
    output_task_x = Text(block_6, width=40, heigh=2,
                         bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    output_task_x.grid(row=2, columnspan=6, sticky=tk.NW)
    output_task_x.configure(state=tk.DISABLED)
    bt_task_x = Button(block_6, text="Go", command=task_x,
                       bg=btn, fg=text3, font=fnt, relief=tk.RIDGE)
    bt_task_x.grid(row=0, column=5, sticky=tk.NE)

    # Example y
    block_7 = Frame(block12, bg=bg_main)
    block_7.grid(row=3, column=2, ipadx=10, ipady=10)
    name7 = Label(block_7, text="Пример 4", bg=bg_main, fg=text2, font=fnt)
    name7.grid(row=0, column=0, ipadx=10, ipady=10, sticky=tk.NW)

    ent_yg = Entry(block_7, width=6,
                   bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_yg.grid(row=1, column=0)
    ent_yg.bind("<FocusIn>", clear)
    lb10 = Label(block_7, text="g^", bg=bg_main, fg=text1, font=fnt)
    lb10.grid(row=1, column=1)
    ent_yx = Entry(block_7, width=6,
                   bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_yx.bind("<FocusIn>", clear)
    ent_yx.grid(row=1, column=2)
    lb11 = Label(block_7, text="x", bg=bg_main, fg=text1, font=fnt)
    lb11.grid(row=1, column=3)
    ent_yp = Entry(block_7, width=6,
                   bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_yp.bind("<FocusIn>", clear)
    ent_yp.grid(row=1, column=4)
    lb12 = Label(block_7, text="(mod p) = y", bg=bg_main, fg=text1, font=fnt)
    lb12.grid(row=1, column=5)
    output_ex_y = Text(block_7, width=40, heigh=2,
                       bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    output_ex_y.grid(row=2, columnspan=6, sticky=tk.NW)
    output_ex_y.configure(state=tk.DISABLED)
    but_ex_y = Button(block_7, text="Go", command=example_y,
                      bg=btn, fg=text3, font=fnt, relief=tk.RIDGE)
    but_ex_y.grid(row=0, column=5, sticky=tk.NE)

    # Task y
    block_8 = Frame(block12, bg=bg_main)
    block_8.grid(row=4, column=2, ipadx=10, ipady=10)
    name8 = Label(block_8, text="Задача 4", bg=bg_main, fg=text2, font=fnt)
    name8.grid(row=0, column=0, ipadx=10, ipady=10, sticky=tk.NW)

    ent_y = Entry(block_8, width=6,
                  bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_y.grid(row=1, column=0)
    ent_y.bind("<FocusIn>", clear)
    py = elg.get_prime_number_in_range(1000, 1100)
    gy = elg.get_primitive_root(py)
    xy = elg.get_prime_number_in_range(1, py - 1)
    lb13 = Label(block_8, text=f"y = {gy} ^ {xy} (mod {py})",
                 bg=bg_main, fg=text1, font=fnt)
    lb13.grid(row=1, column=1)
    output_task_y = Text(block_8, width=40, heigh=2,
                         bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    output_task_y.grid(row=2, columnspan=6, sticky=tk.NW)
    output_task_y.configure(state=tk.DISABLED)
    bt_task_y = Button(block_8, text="Go", command=task_y,
                       bg=btn, fg=text3, font=fnt, relief=tk.RIDGE)
    bt_task_y.grid(row=0, column=5, sticky=tk.NE)
