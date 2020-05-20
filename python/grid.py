#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 21:27
# @Author  : uyplayer
# @Site    : uyplayer.xyz
# @File    : grid.py
# @Software: PyCharm

from tkinter import *

master = Tk()

# Label(master, text="First").grid(row=0)
# Label(master, text="Second").grid(row=1)
#
# e1 = Entry(master)
# e2 = Entry(master)
#
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)



label1.grid(sticky=E)
label2.grid(sticky=E)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

checkbutton.grid(columnspan=2, sticky=W)

image.grid(row=0, column=2, columnspan=2, rowspan=2,
               sticky=W+E+N+S, padx=5, pady=5)

button1.grid(row=2, column=2)
button2.grid(row=2, column=3)

master.mainloop()
master.destroy()