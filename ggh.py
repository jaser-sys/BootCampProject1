from vvv import *
from tkinter import *
import os


class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("UPDATING STATUS")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        chooseButton = Button(self, text="List of Proudcts",command=prod)
        problemButton =Button(self, text="list of problems")
        saveButton = Button(self , text ="Save")
        username =Button(self , text =" username ")
        # placing the button on my window
        chooseButton.place(x=10, y=65)
        problemButton.place(x=10, y=140)
        saveButton.place(x=360 ,y=260)
        username.place(x=9 , y = 9)


root = Tk()

#size of the window
root.geometry("400x300")

app = Window(root)
root.mainloop()