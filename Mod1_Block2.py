import tkinter as tk
from tkinter import Tk, Frame, Button, Label, scrolledtext, Entry, Text
import My_ElGamal as elg
from util import text1, text2, text3, bg_main, bg_entry, btn, fnt, read_text


def click_bt_l_2():

    global win_l_2
    win_l_2 = Tk()
    win_l_2.title("ElGamal signature scheme: Signature")
    win_l_2.geometry("1250x400+50+50")
    win_l_2.minsize(1250, 400)
    win_l_2.config(bg=bg_main)

    def clear(event):
        caller = event.widget
        caller.delete("0", "end")

    def example():
        try:
            output_ex.configure(state=tk.NORMAL)
            ent_m_val = str(ent_m.get())
            ent_p_val = int(ent_p.get())
            ent_g_val = int(ent_g.get())
            ent_x_val = int(ent_x.get())
            output_ex.delete("0.0", "end")
            for i in elg.ds_ElGamal_outp(
                    ent_m_val, ent_p_val, ent_g_val, ent_x_val):
                output_ex.insert("0.0", i)
            output_ex.configure(state=tk.DISABLED)
        except ValueError:
            output_ex.delete("0.0", "end")
            output_ex.insert("0.0", "Введите четыре числа.")
            output_ex.configure(state=tk.DISABLED)

    def task():
        try:
            output_task.configure(state=tk.NORMAL)
            output_task.delete("0.0", "end")
            ent_m2_val = str(ent_m2.get())
            ent_r_val = int(ent_r.get())
            ent_s_val = int(ent_s.get())
            a, b = elg.ds_ElGamal(ent_m2_val, p, g, x)
            if (ent_r_val == a and ent_s_val == b):
                output_task.insert("0.0", "Верно.")
            else:
                output_task.insert("0.0", "Неверно.")
            output_task.configure(state=tk.DISABLED)
        except ValueError:
            output_task.delete("0.0", "end")
            output_task.insert("0.0", "Введите три числа.")
            output_task.configure(state=tk.DISABLED)

    block1 = Frame(win_l_2, bg=bg_main)
    block1.pack(side=tk.LEFT, fill=tk.Y, ipadx=10, ipady=10, expand=1)
    scrlt = scrolledtext.ScrolledText(
        block1, bg=bg_main, fg=text1, font=fnt, relief=tk.FLAT)
    scrlt.pack(side=tk.LEFT, expand=1, fill=tk.Y)
    scrlt.insert(tk.INSERT, read_text("text_mod1_block2.txt"))
    scrlt.configure(state=tk.DISABLED)

    block2 = Frame(win_l_2, bg=bg_main)
    block2.pack(side=tk.RIGHT, fill=tk.Y, ipadx=10, ipady=10, expand=1)

    # Example
    block_top = Frame(block2, bg=bg_main)
    block_top.grid(row=1, column=1)
    lb_t = Label(block_top, text="Пример", bg=bg_main, fg=text2, font=fnt)
    lb_t.grid(row=0, column=0, sticky=tk.NW)
    lb_m = Label(block_top, text="m =", bg=bg_main, fg=text1, font=fnt)
    lb_m.grid(row=1, column=0)
    ent_m = Entry(block_top, width=6,
                  bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_m.grid(row=1, column=1)
    ent_m.bind("<FocusIn>", clear)
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
    lb_x = Label(block_top, text="x =", bg=bg_main, fg=text1, font=fnt)
    lb_x.grid(row=1, column=6)
    ent_x = Entry(block_top, width=6,
                  bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_x.grid(row=1, column=7)
    ent_x.bind("<FocusIn>", clear)
    but_ex = Button(block_top, text="Решить", command=example,
                    bg=btn, fg=text3, font=fnt, relief=tk.RIDGE)
    but_ex.grid(row=1, column=8, sticky=tk.NE)
    output_ex = Text(block_top, width=50, heigh=10,
                     bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    output_ex.grid(row=2, columnspan=9, sticky=tk.NW)
    output_ex.configure(state=tk.DISABLED)

    block_bot = Frame(block2, bg=bg_main)
    block_bot.grid(row=2, column=1)
    lb_b = Label(block_bot, text="Задача", bg=bg_main, fg=text2, font=fnt)
    lb_b.grid(row=0, column=0, sticky=tk.NW)
    lb_p1 = Label(block_bot, text="p =", bg=bg_main, fg=text1, font=fnt)
    lb_p1.grid(row=1, column=0)
    p = elg.get_prime_number_in_range(10, 100)
    lb_p2 = Label(block_bot, text=p, bg=bg_main, fg=text1, font=fnt)
    lb_p2.grid(row=1, column=1)
    lb_g = Label(block_bot, text="g =", bg=bg_main, fg=text1, font=fnt)
    lb_g.grid(row=1, column=2)
    g = elg.get_primitive_root(p)
    lb_g2 = Label(block_bot, text=g, bg=bg_main, fg=text1, font=fnt)
    lb_g2.grid(row=1, column=3)
    lb_x = Label(block_bot, text="x =", bg=bg_main, fg=text1, font=fnt)
    lb_x.grid(row=1, column=4)
    x = elg.get_prime_number_in_range(1, p - 1)
    lb_x = Label(block_bot, text=x, bg=bg_main, fg=text1, font=fnt)
    lb_x.grid(row=1, column=5)
    lb_m2 = Label(block_bot, text="m =", bg=bg_main, fg=text1, font=fnt)
    lb_m2.grid(row=2, column=0)
    ent_m2 = Entry(block_bot, width=6,
                   bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_m2.grid(row=2, column=1)
    ent_m2.bind("<FocusIn>", clear)
    lb_r = Label(block_bot, text="r =", bg=bg_main, fg=text1, font=fnt)
    lb_r.grid(row=2, column=2)
    ent_r = Entry(block_bot, width=6,
                  bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_r.grid(row=2, column=3)
    ent_r.bind("<FocusIn>", clear)
    lb_s = Label(block_bot, text="s =", bg=bg_main, fg=text1, font=fnt)
    lb_s.grid(row=2, column=4)
    ent_s = Entry(block_bot, width=6,
                  bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    ent_s.grid(row=2, column=5)
    ent_s.bind("<FocusIn>", clear)
    but_task = Button(block_bot, text="Проверить", command=task,
                      bg=btn, fg=text3, font=fnt, relief=tk.RIDGE)
    but_task.grid(row=2, column=6, sticky=tk.NE)
    output_task = Text(block_bot, width=50, heigh=3,
                       bg=bg_entry, fg=text1, font=fnt, relief=tk.FLAT)
    output_task.grid(row=3, columnspan=7, sticky=tk.NW)
    output_task.configure(state=tk.DISABLED)
