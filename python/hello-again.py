#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 13:55
# @Author  : uyplayer
# @Site    : uyplayer.xyz
# @File    : hello-again.py
# @Software: PyCharm

from tkinter import *

class APP:

    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame,text="QUIT",fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame,text="Hello",command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print("Hi there im the program ")

root = Tk()
app = APP(root)
root.mainloop()
root.destroy()





