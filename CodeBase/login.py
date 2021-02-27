from tkinter import *
import sys
import os
from login_back import  Database

database = Database("sap.db")

class Window(object):
    def __init__(self,window):
        self.window = window
        self.window.wm_title("Login Screen")

        l0 = Label(window, text="User ID")
        l0.grid(row=0, column=0)

        l1 = Label(window, text="Password")
        l1.grid(row=1, column=0)

        self.id_text = StringVar()
        self.e0 = Entry(window, textvariable=self.id_text)
        self.e0.grid(row=0, column=1)

        self.pass_text = StringVar()
        self.e1 = Entry(window, textvariable=self.pass_text)
        self.e1.grid(row=1, column=1)

        # self.list1 = Listbox(window, height=6, width=35)
        # self.list1.grid(row=3, column=0, rowspan=6, columnspan=2)

        # self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        # now we need to attach a scrollbar to the listbox, and the other direction,too
        # sb1 = Scrollbar(window)
        # sb1.grid(row=2, column=2, rowspan=6)
        # self.list1.config(yscrollcommand=sb1.set)
        # sb1.config(command=self.list1.yview)

        b1 = Button(window, text="Login", width=12, command=self.login_command)
        b1.grid(row=2, column=3)

        # b3 = Button(window, text="Create Account", width=12, command=self.insert_command)
        # b3.grid(row=3, column=3)

        b2 = Button(window, text="Close", width=12, command=window.destroy)
        b2.grid(row=4, column=3)

    def login_command(self):
        if database.login(self.id_text.get(), self.pass_text.get()) == 1:
            window.destroy()
            os.system('python3 homescreen.py')
            
        # self.list1.delete(0, END)
        # self.list1.insert(END, (self.order_id_text.get(), self.sku_text.get(), self.due_text.get(), self.line_id_text.get(), self.inven_text.get(), self.full_text.get()))
    # def insert_command(self):
        # database.insert(self.id_text.get(), )
#code for the GUI (front end)
window = Tk()
Window(window)

window.mainloop()