#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 15:32
# @Author  : uyplayer
# @Site    : uyplayer.xyz
# @File    : Entry.py
# @Software: PyCharm

from tkinter import *

master = Tk()

# e = Entry(master)
# e.pack()
#
# e.focus_set()
#
# def callback():
#     print(e.get())
#
# b = Button(master, text="get", width=10, command=callback)
# b.pack()
#
# mainloop()



e = Entry(master, width=50)
e.pack()

text = e.get()
def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

user = makeentry(parent, "User name:", 10)
password = makeentry(parent, "Password:", 10, show="*")
content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)

text = content.get()
content.set(text)