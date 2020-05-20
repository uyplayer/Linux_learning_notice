#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 14:36
# @Author  : uyplayer
# @Site    : uyplayer.xyz
# @File    : checkbutton.py
# @Software: PyCharm

from tkinter import *

# master = Tk()
# var = IntVar()
# c = Checkbutton(master,text = "Expand",variable=var,onvalue="RGB",offvalue="L")
# c.pack()
# mainloop()

class Cbutton:

    # def __init__(self,master):
    #     self.var = IntVar()
    #     c = Checkbutton(master,text="Enable Tab",variable=self.var,command=self.cd)
    #     c.pack()
    # def cd(self,event):
    #     print("Hello Checkbutton : "+self.var.get())

    def __init__(self, master):
        self.var = IntVar()
        c = Checkbutton(
            master, text="Enable Tab",
            variable=self.var,
            command=self.cb)
        c.pack()

    def cb(self, event):
        print("variable is", self.var.get())



root = Tk()
app = Cbutton(root)
root.mainloop()
root.destroy()



