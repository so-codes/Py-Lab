# Tkinter
Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, and is Python's de facto standard GUI. Tkinter is included with standard Linux, Microsoft Windows and Mac OS X installs of Python.

## Widgets
- Button <br>
If you want to create a button, you can use the Button widget. The Button widget is used to add buttons in your application. The syntax to create a button is given below.

    ```python
    from tkinter import *
    root = Tk()
    b = Button(root, text="Hello")
    b.pack()
    root.mainloop()
    ```

- Canvas
The Canvas widget is used to draw shapes, such as lines, ovals, rectangles, text, and bitmap images. The Canvas widget is useful for drawing graphs and plots, creating graphics editors, and building custom widgets. The syntax to create a canvas is given below.

    ```python
    from tkinter import *
    root = Tk()
    c = Canvas(root, width=200, height=100)
    c.pack()
    c.create_line(0, 0, 200, 100)
    c.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
    c.create_rectangle(50, 25, 150, 75, fill="blue")
    root.mainloop()
    ```

- Checkbutton
The Checkbutton widget is used to display a number of options as check buttons. The syntax to create a checkbutton is given below.

    ```python
    from tkinter import *
    root = Tk()
    v = IntVar()
    c = Checkbutton(root, text="Expand", variable=v)
    c.pack()
    root.mainloop()
    ```

- Entry
The Entry widget is used to accept single-line text strings from a user. The syntax to create an entry is given below.

    ```python
    from tkinter import *
    root = Tk()
    e = Entry(root)
    e.pack()
    e.focus_set()
    def callback():
        print(e.get())
    b = Button(root, text="get", width=10, command=callback)
    b.pack()
    root.mainloop()
    ```

- Frame
The Frame widget is used as a container widget to organize other widgets. The syntax to create a frame is given below.

    ```python
    from tkinter import *
    root = Tk()
    f = Frame(root)
    f.pack()
    left = Frame(f)
    left.pack(side=LEFT)
    right = Frame(f)
    right.pack(side=RIGHT)
    Button(left, text="Hello").pack()
    Button(right, text="World").pack()
    root.mainloop()
    ```

- Label
The Label widget is used to provide a single-line caption for another widget. The syntax to create a label is given below.

    ```python
    from tkinter import *
    root = Tk()
    w = Label(root, text="Hello, world!")
    w.pack()
    root.mainloop()
    ```

- Listbox
The Listbox widget is used to display a list of items from which a user may select one or more items. The syntax to create a listbox is given below.

    ```python
    from tkinter import *
    root = Tk()
    lb = Listbox(root)
    lb.pack()
    lb.insert(END, "a list entry")
    lb.insert(END, "another list entry")
    lb.insert(END, "a third list entry")
    root.mainloop()
    ```

- Menu
The Menu widget is used to create a menu bar, a pull-down menu, or a pop-up menu. The syntax to create a menu is given below.

    ```python
    from tkinter import *
    root = Tk()
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=do_nothing)
    filemenu.add_command(label="Save", command=do_nothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=do_nothing)
    editmenu.add_separator()
    editmenu.add_command(label="Cut", command=do_nothing)
    editmenu.add_command(label="Copy", command=do_nothing)
    editmenu.add_command(label="Paste", command=do_nothing)
    editmenu.add_command(label="Delete", command=do_nothing)
    editmenu.add_command(label="Select All", command=do_nothing)

    menubar.add_cascade(label="Edit", menu=editmenu)
    ```
    
- Menubutton
The Menubutton widget is used to display a menu when pressed. The syntax to create a menubutton is given below.

    ```python
    from tkinter import *
    root = Tk()
    mb = Menubutton(root, text="condiments", relief=RAISED)
    mb.grid()
    mb.menu = Menu(mb, tearoff=0)
    mb["menu"] = mb.menu
    ketch = IntVar()
    mustard = IntVar()
    mb.menu.add_checkbutton(label="Ketchup", variable=ketch)
    mb.menu.add_checkbutton(label="Mustard", variable=mustard)
    mb.pack()
    root.mainloop()
    ```

- Message
The Message widget is used to display multiline text that cannot be edited. The syntax to create a message is given below.

    ```python
    from tkinter import *
    root = Tk()
    w = Message(root, text="This is a message")
    w.pack()
    root.mainloop()
    ```

- Radiobutton
The Radiobutton widget is used to display a number of options as radio buttons. The syntax to create a radiobutton is given below.

    ```python
    from tkinter import *
    root = Tk()
    v = IntVar()
    v.set(1)
    languages = [
        ("Python", 1),
        ("Perl", 2),
        ("Java", 3),
        ("C++", 4),
        ("C", 5)
    ]
    def ShowChoice():
        print(v.get())
    Label(root, 
          text="Choose your favourite"
          ).pack()

    for txt, val in languages:
        Radiobutton(root, 
                    text=txt,
                    indicatoron=0,
                    width=20,
                    padx=20, 
                    variable=v, 
                    command=ShowChoice,
                    value=val).pack(anchor=W)
    root.mainloop()
    ```

- Scale
The Scale widget is used to select a value from a range. The syntax to create a scale is given below.

    ```python
    from tkinter import *
    root = Tk()
    w = Scale(root, from_=0, to=42)
    w.pack()
    w = Scale(root, from_=0, to=200, orient=HORIZONTAL)
    w.pack()
    root.mainloop()
    ```

- Scrollbar
The Scrollbar widget is used to provide a scroll bar for another widget. The syntax to create a scrollbar is given below.

    ```python
    from tkinter import *
    root = Tk()
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    mylist = Listbox(root, yscrollcommand=scrollbar.set)
    for line in range(100):
        mylist.insert(END, "This is line number " + str(line))
    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)
    root.mainloop()
    ```

- Text
The Text widget is used to display multiple lines of text that can be edited. The syntax to create a text is given below.

    ```python
    from tkinter import *
    root = Tk()
    T = Text(root, height=2, width=30)
    T.pack()
    T.insert(END, "Just a text Widget\nin two lines\n")
    mainloop()
    ```

- Toplevel
The Toplevel widget is used to create a new window. The syntax to create a toplevel is given below.

    ```python
    from tkinter import *
    root = Tk()
    top = Toplevel()
    top.title("New Window")
    top.mainloop()
    ```

- Spinbox
The Spinbox widget is used to select a value from a range of values. The syntax to create a spinbox is given below.

    ```python
    from tkinter import *
    root = Tk()
    w = Spinbox(root, from_=0, to=10)
    w.pack()
    root.mainloop()
    ```

- PanedWindow
The PanedWindow widget is used to create a window with multiple panes. The syntax to create a panedwindow is given below.

    ```python
    from tkinter import *
    root = Tk()
    pw = PanedWindow()
    pw.pack(fill=BOTH, expand=1)
    left = Label(pw, text="left pane")
    pw.add(left)
    pw2 = PanedWindow(pw, orient=VERTICAL)
    pw.add(pw2)
    top = Label(pw2, text="top pane")
    pw2.add(top)
    bottom = Label(pw2, text="bottom pane")
    pw2.add(bottom)
    root.mainloop()
    ```

- LabelFrame
The LabelFrame widget is used to group related widgets in a frame. The syntax to create a labelframe is given below.

    ```python
    from tkinter import *
    root = Tk()
    lf = LabelFrame(root, text="My Frame")
    lf.pack(fill="both", expand="yes")
    left = Label(lf, text="Inside the frame")
    left.pack()
    root.mainloop()
    ```

- MessageBox
The messagebox widget is used to display a message box. The syntax to create a messagebox is given below.

    ```python
    from tkinter import *
    from tkinter import messagebox
    root = Tk()
    messagebox.showinfo("Hello Python", "Hello World")
    root.mainloop()
    ```
