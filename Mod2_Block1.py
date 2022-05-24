import tkinter as tk
from tkinter import Tk, Frame, Button, Label, scrolledtext, Entry, Text
import My_DiscrtLog as dis
from util import text1, text2, text3, bg_main, bg_entry, btn, fnt, read_text, get_values


def click_bt_r_1():

    global win_r_1
    win_r_1 = Tk()
    win_r_1.title("Computing discrete logarithm: Coherence Method")
    win_r_1.geometry("1250x400+50+50")
    win_r_1.minsize(1200, 400)
    win_r_1.config(bg=bg_main)

    def clear(event):
        caller = event.widget
        caller.delete("0", "end")

    def example():
        try:
            output_ex.configure(state=tk.NORMAL)
            ent_a_val = int(ent_a.get())
            ent_b_val = int(ent_b.get())
            ent_n_val = int(ent_n.get())
            output_ex.delete("0.0", "end")
            for i in dis.coherence_method_output(
                    ent_a_val, ent_b_val, ent_n_val):
                output_ex.insert("0.0", i)
            output_ex.configure(state=tk.DISABLED)
        except ValueError:
            output_ex.delete("0.0", "end")
            output_ex.insert("0.0", "Введите три числа.")
            output_ex.configure(state=tk.DISABLED)

    def task():
        try:
            output_task.configure(state=tk.NORMAL)
            output_task.delete("0.0", "end")
            ent_x_val = int(ent_x.get())
            x = dis.coherence_method(values[0], values[1], values[2])
            if (x == ent_x_val):
                output_task.insert("0.0", "Верно.")
            else:
                output_task.insert("0.0", "Неверно.")
            output_task.configure(state=tk.DISABLED)
        except ValueError:
            output_task.delete("0.0", "end")
            output_task.insert("0.0", "Введите число.")
            output_task.configure(state=tk.DISABLED)

    block1 = Frame(win_r_1, bg=bg_main)
    block1.pack(side=tk.LEFT, fill=tk.Y, ipadx=10, ipady=10, expand=1)
    scrlt = scrolledtext.ScrolledText(
        block1, bg=bg_main, fg=text1, font=fnt, relief=tk.FLAT)
    scrlt.pack(side=tk.LEFT, expand=1, fill=tk.Y)
    scrlt.insert(tk.INSERT, read_text("text_mod2_block1.txt"))
    scrlt.configure(state=tk.DISABLED)

    block2 = Frame(win_r_1, bg=bg_main)
    block2.pack(side=tk.RIGHT, fill=tk.Y, ipadx=10, ipady=10, expand=1)

    # Example
    block_top = Frame(block2, bg=bg_main)
    block_top.grid(row=1, column=1)
    name1 = Label(block_top, text="Пример", bg=bg_main, fg=text2, font=fnt)
    name1.grid(row=0, column=0, sticky=tk.NW)
    lb_1 = Label(block_top, text="a", bg=bg_main, fg=text1, font=fnt)
    lb_1.grid(row=1, column=0)
    ent_a = Entry(block_top, width=6,
                  bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_a.grid(row=1, column=1)
    ent_a.bind("<FocusIn>", clear)
    lb_2 = Label(block_top, text="^ x ≡ b", bg=bg_main, fg=text1, font=fnt)
    lb_2.grid(row=1, column=2)
    ent_b = Entry(block_top, width=6,
                  bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_b.grid(row=1, column=3)
    ent_b.bind("<FocusIn>", clear)
    lb_3 = Label(block_top, text="(mod n)", bg=bg_main, fg=text1, font=fnt)
    lb_3.grid(row=1, column=4)
    ent_n = Entry(block_top, width=6,
                  bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_n.grid(row=1, column=5)
    ent_n.bind("<FocusIn>", clear)
    but_ex = Button(block_top, text="Решить", command=example,
                    bg=btn, fg=text3, font=fnt, relief=tk.RIDGE)
    but_ex.grid(row=1, column=6, sticky=tk.NE)
    output_ex = Text(block_top, width=50, heigh=11,
                     bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    output_ex.grid(row=2, columnspan=7, sticky=tk.NW)
    output_ex.configure(state=tk.DISABLED)

    # Task
    block_bot = Frame(block2, bg=bg_main)
    block_bot.grid(row=2, column=1)
    name2 = Label(block_bot, text="Задача", bg=bg_main, fg=text2, font=fnt)
    name2.grid(row=0, column=0, sticky=tk.NW)

    values = get_values(1)[0]

    lb_11 = Label(block_bot, text=f"{values[0]}^",
                  bg=bg_main, fg=text1, font=fnt)
    lb_11.grid(row=1, column=0)
    ent_x = Entry(block_bot, width=6,
                  bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_x.grid(row=1, column=1)
    ent_x.bind("<FocusIn>", clear)
    lb_22 = Label(block_bot, text=f"≡ {values[1]} (mod {values[2]})",
                  bg=bg_main, fg=text1, font=fnt)
    lb_22.grid(row=1, column=3)
    but_task = Button(block_bot, text="Проверить", command=task,
                      bg=btn, fg=text3, font=fnt, relief=tk.RIDGE)
    but_task.grid(row=1, column=4, sticky=tk.NE)
    output_task = Text(block_bot, width=50, heigh=2,
                       bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    output_task.grid(row=2, columnspan=5, sticky=tk.NW)
    output_task.configure(state=tk.DISABLED)
