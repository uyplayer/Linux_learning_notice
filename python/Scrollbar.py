#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 20:43
# @Author  : uyplayer
# @Site    : uyplayer.xyz
# @File    : Scrollbar.py
# @Software: PyCharm

from tkinter import *

master = Tk()

scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(master, yscrollcommand=scrollbar.set)
for i in range(1000):
    listbox.insert(END, str(i))
listbox.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=listbox.yview)

mainloop()