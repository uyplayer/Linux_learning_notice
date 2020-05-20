#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 15:49
# @Author  : uyplayer
# @Site    : uyplayer.xyz
# @File    : Text.py
# @Software: PyCharm

from tkinter import *

root = Tk()
text = Text(root,width=20,height=15)
text.pack()
text.insert(INSERT,"Text here \n")
text.insert(END,"there ")
mainloop()