# Design a program to create a menubar with following structure

# File New, Open, Save

# Edit Cut Copy Paste

# View Freeze, Zoom, | Preferences

from tkinter import *

root = Tk()

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")

filemenu.add_separator()

filemenu.add_command(label="Save")
filemenu.add_command(label="Save as...")
filemenu.add_command(label="Close")

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Delete")
editmenu.add_command(label="Select All")

menubar.add_cascade(label="Edit", menu=editmenu)

viewmenu = Menu(menubar, tearoff=0)
viewmenu.add_command(label="Freeze")
viewmenu.add_command(label="Zoom")
viewmenu.add_command(label="Preferences")

menubar.add_cascade(label="View", menu=viewmenu)

root.config(menu=menubar)

root.mainloop()



