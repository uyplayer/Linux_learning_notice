#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 19:15
# @Author  : uyplayer
# @Site    : uyplayer.xyz
# @File    : Frame.py
# @Software: PyCharm

from tkinter import *

master = Tk()

Label(text="one").pack()

separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

Label(text="two").pack()

mainloop()

