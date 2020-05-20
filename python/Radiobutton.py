#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 15:02
# @Author  : uyplayer
# @Site    : uyplayer.xyz
# @File    : Radiobutton.py
# @Software: PyCharm

from tkinter import *

master = Tk()

v = IntVar()


'''
Radiobutton(master, text="One", variable=v, value=1).pack(anchor=W)
Radiobutton(master, text="Two", variable=v, value=2).pack(anchor=W)
'''
Radiobutton(master, text="One", variable=v, value=1,indicatoron=0).pack(anchor=W)
Radiobutton(master, text="Two", variable=v, value=2,indicatoron=0).pack(anchor=W)

mainloop()