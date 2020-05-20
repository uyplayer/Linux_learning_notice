#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 20:55
# @Author  : uyplayer
# @Site    : uyplayer.xyz
# @File    : Spinbox.py
# @Software: PyCharm

from tkinter import *

master = Tk()

w = Spinbox(master, from_=0, to=10)
w.pack()

mainloop()