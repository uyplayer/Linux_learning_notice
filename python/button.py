#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 14:32
# @Author  : uyplayer
# @Site    : uyplayer.xyz
# @File    : button.py
# @Software: PyCharm

from tkinter import *

master = Tk()
f = Frame(master, height=32, width=32)
def callback(event):
    print("click!")

# b = Button(master, text="OK", command=callback)
b = Button(f, text="Help", state=DISABLED)
b.pack()


mainloop()