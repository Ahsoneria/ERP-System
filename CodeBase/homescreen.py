import sys
import os
from tkinter import *
import tkinter.ttk as ttk 
from tkinter.font import Font
# from inven_back import  Database
# from tkinter.ttk import *

# database = Database("sap.db")

class Window(object):
    def __init__(self,window):
        self.window = window
        self.window.wm_title("Home Screen")

        myFont = Font(family="Times New Roman", size=25)
        myFont_2 = Font(family="Times New Roman", size=19)
        myFont_3 = Font(family="Times New Roman", size=25)

        ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=7, columnspan=7, sticky='we')
        ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=8, columnspan=7, sticky='we')
        ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=9, columnspan=7, sticky='we')
        ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=10, columnspan=7, sticky='we')
        ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=11, columnspan=7, sticky='we')

        l10 = Label(window, text="Home Screen", font=myFont_3)
        l10.grid(row=12, column=0,rowspan=2,columnspan=3, pady=10)
        l10.config(bg="burlywood4", fg="black")
        # l10.config(bg="black", fg="white")

        l11 = Label(window, text="Sai Bhandar", font=myFont_3)
        l11.grid(row=14, column=0,rowspan=2,columnspan=3, pady=10)
        l11.config(bg="burlywood4", fg="black")

        b1 = Button(window, text="Employee", font=myFont, height = 5, width=32, command=self.emp_command)
        b1.grid(row=0, column=0, padx=20, pady=20)
        # b1.config(bg="burlywood4", fg="black")

        b2 = Button(window, text="Supplier", font=myFont, height = 5, width=32,command=self.sup_command)
        b2.grid(row=1, column=0, padx=20, pady=20)
        # b2.config(bg="burlywood4", fg="black")

        b3 = Button(window, text="Customer", font=myFont, height = 5, width=32,command=self.cus_command)
        b3.grid(row=2, column=0, padx=20, pady=20)
        # b3.config(bg="burlywood4", fg="black")

        b4 = Button(window, text="Inventory", font=myFont, height = 5, width=32,command=self.inven_command)
        b4.grid(row=0, column=1, padx=20, pady=20)
        # b4.config(bg="burlywood4", fg="black")

        b5 = Button(window, text="Product", font=myFont, height = 5, width=32,command=self.prod_command)
        b5.grid(row=1, column=1, padx=20, pady=20)
        # b5.config(bg="burlywood4", fg="black")

        b6 = Button(window, text="Product Category", font=myFont, height = 5, width=32,command=self.prodcat_command)
        b6.grid(row=2, column=1, padx=20, pady=20)
        # b6.config(bg="burlywood4", fg="black")

        b7 = Button(window, text="Location", font=myFont, height = 5, width=32,command=self.loc_command)
        b7.grid(row=0, column=2, padx=20, pady=20)
        # b7.config(bg="AntiqueWhite1", fg="black")

        b8 = Button(window, text="Order Header", font=myFont, height = 5, width=32,command=self.order_head_command)
        b8.grid(row=1, column=2, padx=20, pady=20)
        # b8.config(bg="AntiqueWhite2", fg="black")

        b9 = Button(window, text="Order Line", font=myFont, height = 5, width=32,command=self.order_line_command)
        b9.grid(row=2, column=2, padx=20, pady=20)
        # b9.config(bg="AntiqueWhite3", fg="black")

        # b10 = Button(window, text="Log Out", font=myFont, height = 2, width=32,command=self.logout)
        # b10.grid(row=3, column=1, padx=20, pady=20)
        # # b10.config(bg="burlywood4", fg="black")

        b11 = Button(window, text="Close", height = 2,width=32, command=window.destroy, font=myFont)
        b11.grid(row=3, column=2,padx=20, pady=20)
        # b11.config(bg="burlywood4", fg="black")

        b12 = Button(window, text="Accounts", font=myFont, height = 2, width=68,command=self.acc_command)
        b12.grid(row=3, column=0, columnspan=2, padx=20, pady=20)
        # b12.config(bg="burlywood2", fg="black")

    def acc_command(self):
        os.system('python3 acc.py')

    def emp_command(self):
        os.system('python3 emp.py')

    def sup_command(self):
        os.system('python3 sup.py')

    def cus_command(self):
        os.system('python3 cus.py')
    def inven_command(self):
        os.system('python3 inven.py')
    def prod_command(self):
        os.system('python3 prod.py')
    def prodcat_command(self):
        os.system('python3 procat.py')
    def loc_command(self):
        os.system('python3 loc.py')
    def order_head_command(self):
        os.system('python3 order_header.py')
    def order_line_command(self):
        os.system('python3 order_line.py')
    def logout(self):
        window.destroy()
        os.system('python3 login.py')


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

#code for the GUI (front end)
window = Tk()
window.configure(bg="burlywood4")
# window.configure(bg="black")
# window = ThemedTk(theme="black")
# window.style = Style()
# #('clam', 'alt', 'default', 'classic')
# window.style.theme_use("clam")

# style = ThemedStyle(window)
# style.theme_use("arc")
# style.theme_use("black")  # only changes the theme of the ttk widgets
# change style of tk widgets manually:
# bg = style.lookup('TLabel', 'background')
# fg = style.lookup('TLabel', 'foreground')
# window.configure(bg='SkyBlue1')
# Window(window)

# window.mainloop()
def main():
  Window(window)
  app=FullScreenApp(window)
  # s=ttk.Style()
  # print(s.theme_use('clam'))
  # s = ttk.Style()
  # s.theme_use('clam')
  # style = ThemedStyle(window)
  # style.set_theme("scidgrey")
  window.mainloop()

if __name__ == "__main__":
  main()