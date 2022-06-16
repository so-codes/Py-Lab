# Widget Type and their configuration

from tkinter import *
root = Tk()

labelfont = ('times', 20, 'bold')
widget = Label(root, text='I like rust')
widget.config(bg='black', fg='yellow')
widget.config(font=labelfont)
widget.config(height=3, width=20)
widget.pack(expand=YES, fill=BOTH)

button = Button(root, text='Click me!')
button.config(bg='black', fg='yellow')
button.config(font=labelfont)
button.config(height=3, width=20)
button.pack(expand=YES, fill=BOTH)

radio = Radiobutton(root, text='I like rust')
radio.config(bg='black', fg='yellow')
radio.config(font=labelfont)
radio.config(height=3, width=10)
radio.pack(expand=YES)


root.mainloop()