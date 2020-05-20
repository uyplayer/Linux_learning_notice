#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 20:36
# @Author  : uyplayer
# @Site    : uyplayer.xyz
# @File    : Scale.py
# @Software: PyCharm

from tkinter import *

master = Tk()

w = Scale(master, from_=0, to=100)
w.pack()
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()
mainloop()
w = Scale(master, from_=0, to=100)
w.pack()

print(w.get())