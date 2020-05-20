#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 20:30
# @Author  : uyplayer
# @Site    : uyplayer.xyz
# @File    : Message.py
# @Software: PyCharm

from tkinter import *

master = Tk()

w = Message(master, text="this is a relatively long message", width=560)
w.pack()

mainloop()