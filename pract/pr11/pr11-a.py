# Configuring widgets

from tkinter import *
root = Tk()

labelfont = ('times', 20, 'bold')
widget = Label(root, text='I like rust')
widget.config(bg='black', fg='yellow')
widget.config(font=labelfont)
widget.config(height=3, width=20)
widget.pack(expand=YES, fill=BOTH)

root.mainloop()