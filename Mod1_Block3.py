import tkinter as tk
from tkinter import Tk, Frame, Button, Label, scrolledtext, Entry, Text
import My_ElGamal as elg
import random
from util import text1, text2, text3, bg_main, bg_entry, btn, fnt, read_text


def click_bt_l_3():

    global win_l_3
    win_l_3 = Tk()
    win_l_3.title("ElGamal signature scheme: Verification")
    win_l_3.geometry("1250x450+50+50")
    win_l_3.minsize(1200, 450)
    win_l_3.config(bg=bg_main)

    def clear(event):
        caller = event.widget
        caller.delete("0", "end")

    def example():
        try:
            output_ex.configure(state=tk.NORMAL)
            ent_m_val = str(ent_m.get())
            ent_y_val = int(ent_y.get())
            ent_p_val = int(ent_p.get())
            ent_g_val = int(ent_g.get())
            ent_r_val = int(ent_r.get())
            ent_s_val = int(ent_s.get())
            output_ex.delete("0.0", "end")
            for i in elg.check_ds_ElGamal_outp(
                    ent_m_val, ent_r_val, ent_s_val, ent_y_val, ent_g_val, ent_p_val):
                output_ex.insert("0.0", i)
            output_ex.configure(state=tk.DISABLED)
        except ValueError:
            output_ex.delete("0.0", "end")
            output_ex.insert("0.0", "Введите шесть чисел.")
            output_ex.configure(state=tk.DISABLED)

    def task():
        try:
            output_task.configure(state=tk.NORMAL)
            output_task.delete("0.0", "end")
            if (elg.check_ds_ElGamal(m, r, s, y, g, p)):
                output_task.insert("0.0", "Подпись подлинна.")
            else:
                output_task.insert("0.0", "Подпись подделана.")
            output_task.configure(state=tk.DISABLED)
        except ValueError:
            output_task.delete("0.0", "end")
            output_task.configure(state=tk.DISABLED)

    block1 = Frame(win_l_3, bg=bg_main)
    block1.pack(side=tk.LEFT, fill=tk.Y, ipadx=10, ipady=10, expand=1)
    scrlt = scrolledtext.ScrolledText(
        block1, bg=bg_main, fg=text1, font=fnt, relief=tk.FLAT)
    scrlt.pack(side=tk.LEFT, expand=1, fill=tk.Y)
    scrlt.insert(tk.INSERT, read_text("text_mod1_block3.txt"))
    scrlt.configure(state=tk.DISABLED)

    block2 = Frame(win_l_3, bg=bg_main)
    block2.pack(side=tk.RIGHT, fill=tk.Y, ipadx=10, ipady=10, expand=1)

    # Example
    block_top = Frame(block2, bg=bg_main)
    block_top.grid(row=1, column=1)
    lb_t = Label(block_top, text="Пример", bg=bg_main, fg=text2, font=fnt)
    lb_t.grid(row=0, column=0, sticky=tk.NW)
    lb_y = Label(block_top, text="y =", bg=bg_main, fg=text1, font=fnt)
    lb_y.grid(row=1, column=0)
    ent_y = Entry(block_top, width=6,
                  bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_y.grid(row=1, column=1)
    ent_y.bind("<FocusIn>", clear)
    lb_p = Label(block_top, text="p =", bg=bg_main, fg=text1, font=fnt)
    lb_p.grid(row=1, column=2)
    ent_p = Entry(block_top, width=6,
                  bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_p.grid(row=1, column=3)
    ent_p.bind("<FocusIn>", clear)
    lb_g = Label(block_top, text="g =", bg=bg_main, fg=text1, font=fnt)
    lb_g.grid(row=1, column=4)
    ent_g = Entry(block_top, width=6,
                  bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_g.grid(row=1, column=5)
    ent_g.bind("<FocusIn>", clear)
    lb_m = Label(block_top, text="m =", bg=bg_main, fg=text1, font=fnt)
    lb_m.grid(row=2, column=0)
    ent_m = Entry(block_top, width=6,
                  bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_m.grid(row=2, column=1)
    ent_m.bind("<FocusIn>", clear)
    lb_r = Label(block_top, text="r =", bg=bg_main, fg=text1, font=fnt)
    lb_r.grid(row=2, column=2)
    ent_r = Entry(block_top, width=6,
                  bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_r.grid(row=2, column=3)
    ent_r.bind("<FocusIn>", clear)
    lb_s = Label(block_top, text="s =", bg=bg_main, fg=text1, font=fnt)
    lb_s.grid(row=2, column=4)
    ent_s = Entry(block_top, width=6,
                  bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_s.grid(row=2, column=5)
    ent_s.bind("<FocusIn>", clear)
    but_ex = Button(block_top, text="Решить", command=example,
                    bg=btn, fg=text3, font=fnt, relief=tk.RIDGE)
    but_ex.grid(row=2, column=6, sticky=tk.NE)
    output_ex = Text(block_top, width=50, heigh=10,
                     bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    output_ex.grid(row=3, columnspan=7, sticky=tk.NW)
    output_ex.configure(state=tk.DISABLED)

    # Task y
    block_bot = Frame(block2, bg=bg_main)
    block_bot.grid(row=2, column=1)
    lb_b = Label(block_bot, text="Задача", bg=bg_main, fg=text2, font=fnt)
    lb_b.grid(row=0, column=0, sticky=tk.NW)

    y, p, g, x = elg.get_keys_ElGamal(10, 100)
    flag = random.randint(0, 1)
    if (flag):
        x = p + 6
    m = elg.get_random_message(6)
    r, s = elg.ds_ElGamal(m, p, g, x)
    lb_y2 = Label(block_bot, text=f"y = {y}", bg=bg_main, fg=text1, font=fnt)
    lb_y2.grid(row=1, column=0)
    lb_p2 = Label(block_bot, text=f"p = {p}", bg=bg_main, fg=text1, font=fnt)
    lb_p2.grid(row=1, column=2)
    lb_g2 = Label(block_bot, text=f"g = {g}", bg=bg_main, fg=text1, font=fnt)
    lb_g2.grid(row=1, column=4)
    lb_m2 = Label(block_bot, text=f"m = {m}", bg=bg_main, fg=text1, font=fnt)
    lb_m2.grid(row=2, column=0)
    lb_r2 = Label(block_bot, text=f"r = {r}", bg=bg_main, fg=text1, font=fnt)
    lb_r2.grid(row=2, column=2)
    lb_s2 = Label(block_bot, text=f"s = {s}", bg=bg_main, fg=text1, font=fnt)
    lb_s2.grid(row=2, column=4)
    but_task = Button(block_bot, text="Проверить", command=task,
                      bg=btn, fg=text3, font=fnt, relief=tk.RIDGE)
    but_task.grid(row=2, column=6, sticky=tk.NE)
    output_task = Text(block_bot, width=50, heigh=3,
                       bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    output_task.grid(row=3, columnspan=7, sticky=tk.NW)
    output_task.configure(state=tk.DISABLED)
