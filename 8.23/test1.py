#coding=utf-8
from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
        # self.onclick()

    def createWidgets(self):
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.commit=Button(self,text='commit',command=self.onclick)
        self.commit.pack()

    def onclick(self):
        name=self.nameInput.get() or 'world'
        messagebox.showinfo('message','hello,%s' %name)




app=Application()
app.master.title('my window')
app.master.geometry('600x600')
app.mainloop()
