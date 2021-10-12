from tkinter import *
from tkinter import messagebox as msg


class App:

    def __init__(self, parent):
        self.widgets(parent)

    def widgets(self, app):
        self.title = Label(app, text='Enter Your Name').pack()
        self.name = StringVar()
        self.entry = Entry(app, textvariable=self.name).pack()
        self.btn = Button(app, text='Say Hi!', command=self.say_hi).pack()

    def say_hi(self):
        name = self.name.get()
        msg.showinfo("Hello {}!!!".format(name.upper()))


root = Tk()
object = App(root)
root.mainloop()
