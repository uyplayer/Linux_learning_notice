#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 20:47
# @Author  : uyplayer
# @Site    : uyplayer.xyz
# @File    : Toplevel.py
# @Software: PyCharm


from tkinter import *

root = Tk()

top = Toplevel()
top.title("About this application...")

msg = Message(top, text="Hellooooo")
msg.pack()

button = Button(top, text="Dismiss", command=top.destroy)
button.pack()
mainloop()