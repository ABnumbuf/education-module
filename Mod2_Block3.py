import tkinter as tk
from tkinter import Tk, Frame, Button, Label, Entry, Text
import My_DiscrtLog as dis
from util import text1, text2, text3, bg_main, bg_entry, btn, fnt
from execution_times import get_values, method_mean_execution_time


def click_bt_r_3():

    global win_r_3
    win_r_3 = Tk()
    win_r_3.title("Computing discrete logarithm: Execution times")
    win_r_3.geometry("800x170+50+50")
    win_r_3.minsize(800, 170)
    win_r_3.config(bg=bg_main)

    def clear(event):
        caller = event.widget
        caller.delete("0", "end")

    def task1():
        try:
            output_1.configure(state=tk.NORMAL)
            ent_t1_val = int(ent_t1.get())
            ent_da1_val = int(ent_da1.get())
            ent_db1_val = int(ent_db1.get())
            values = get_values(ent_t1_val, ent_da1_val, ent_db1_val)
            res1 = method_mean_execution_time(
                dis.coherence_method, values)
            output_1.delete("0.0", "end")
            output_1.insert("0.0", f"Среднее время выполнения: {res1} сек")
            output_1.configure(state=tk.DISABLED)
        except ValueError:
            output_1.delete("0.0", "end")
            output_1.insert("0.0", "Введите три числа.")
            output_1.configure(state=tk.DISABLED)

    def task2():
        try:
            output_2.configure(state=tk.NORMAL)
            ent_t2_val = int(ent_t2.get())
            ent_da2_val = int(ent_da2.get())
            ent_db2_val = int(ent_db2.get())
            values = get_values(ent_t2_val, ent_da2_val, ent_db2_val)
            res2 = method_mean_execution_time(
                dis.sylvester_pohlig_hellman_method, values)
            output_2.delete("0.0", "end")
            output_2.insert("0.0", f"Среднее время выполнения: {res2} сек")
            output_2.configure(state=tk.DISABLED)
        except ValueError:
            output_2.delete("0.0", "end")
            output_2.insert("0.0", "Введите три числа")
            output_2.configure(state=tk.DISABLED)

    block1 = Frame(win_r_3, bg=bg_main)
    block1.pack(side=tk.LEFT, fill=tk.Y, ipadx=10, ipady=10, expand=1)
    block2 = Frame(win_r_3, bg=bg_main)
    block2.pack(side=tk.RIGHT, fill=tk.Y, ipadx=10, ipady=10, expand=1)

    name1 = Label(block1, text="Метод согласования",
                  bg=bg_main, fg=text2, font=("consolas", 14))
    name1.grid(row=0, columnspan=3, sticky=tk.NW)
    lb_1 = Label(block1, text="Количество тестов:",
                 bg=bg_main, fg=text1, font=fnt)
    lb_1.grid(row=1, column=0, sticky=tk.NW)
    ent_t1 = Entry(block1, width=6,
                   bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_t1.grid(row=1, column=1, sticky=tk.NW)
    ent_t1.bind("<FocusIn>", clear)
    lb_2 = Label(block1, text="Диапазон:", bg=bg_main, fg=text1, font=fnt)
    lb_2.grid(row=2, column=0, sticky=tk.NW)
    ent_da1 = Entry(block1, width=6,
                    bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_da1.grid(row=2, column=1, sticky=tk.NW)
    ent_da1.bind("<FocusIn>", clear)
    ent_db1 = Entry(block1, width=6,
                    bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_db1.grid(row=2, column=2, sticky=tk.NW)
    ent_db1.bind("<FocusIn>", clear)
    but_1 = Button(block1, text="Измерить", command=task1,
                   bg=btn, fg=text3, font=fnt, relief=tk.RIDGE)
    but_1.grid(row=1, column=2, sticky=tk.NE)
    output_1 = Text(block1, width=35, heigh=3,
                    bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    output_1.grid(row=3, columnspan=3, sticky=tk.NW)
    output_1.configure(state=tk.DISABLED)

    name2 = Label(block2, text="Метод Сильвестра-Полига-Хеллмана",
                  bg=bg_main, fg=text2, font=("consolas", 14))
    name2.grid(row=0, columnspan=3, sticky=tk.NW)
    lb_3 = Label(block2, text="Количество тестов:",
                 bg=bg_main, fg=text1, font=fnt)
    lb_3.grid(row=1, column=0, sticky=tk.NW)
    ent_t2 = Entry(block2, width=6,
                   bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_t2.grid(row=1, column=1, sticky=tk.NW)
    ent_t2.bind("<FocusIn>", clear)
    lb_4 = Label(block2, text="Диапазон:", bg=bg_main, fg=text1, font=fnt)
    lb_4.grid(row=2, column=0, sticky=tk.NW)
    ent_da2 = Entry(block2, width=6,
                    bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_da2.grid(row=2, column=1, sticky=tk.NW)
    ent_da2.bind("<FocusIn>", clear)
    ent_db2 = Entry(block2, width=6,
                    bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_db2.grid(row=2, column=2, sticky=tk.NW)
    ent_db2.bind("<FocusIn>", clear)
    but_2 = Button(block2, text="Измерить", command=task2,
                   bg=btn, fg=text3, font=fnt, relief=tk.RIDGE)
    but_2.grid(row=1, column=2, sticky=tk.NE)
    output_2 = Text(block2, width=35, heigh=3,
                    bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    output_2.grid(row=3, columnspan=3, sticky=tk.NW)
    output_2.configure(state=tk.DISABLED)
