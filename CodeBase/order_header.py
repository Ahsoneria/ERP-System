from tkinter import *
from order_header_back import  Database
from tkinter.font import Font
import tkinter.ttk as ttk
database = Database("sap.db")

import os
# box_value = StringVar()
        # def fun():
        #     print(box_value.get())
        # combo = AutocompleteCombobox(textvariable=box_value)
        # test_list = ['apple', 'appy2', 'apple pie', 'apple juice', 'appy', 'banana', 'cherry', 'grapes']
        # combo.set_completion_list(test_list)
        # combo.grid(row=1,column=5)
        # button = Button(text='but', command=fun)
        # button.grid(row=2,column=5)
class Window(object):
    def __init__(self,window):
        self.window = window
        self.window.wm_title("Order Header Screen")

        myFont = Font(family="Times New Roman", size=21)
        myFont_2 = Font(family="Times New Roman", size=19)
        myFont_3 = Font(family="Times New Roman", size=23)

        ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=9, columnspan=7, sticky='we')
        ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=10, columnspan=7, sticky='we')
        ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=11, columnspan=7, sticky='we')

        l10 = Label(window, text="Order Header Screen", font=myFont_3)
        l10.grid(row=12, column=2,rowspan=2,columnspan=2, pady=40)
        # l10.config(bg="black", fg="white")
        l10.config(bg="burlywood4", fg="black")

        l11 = Label(window, text="Sai Bhandar", font=myFont_3)
        l11.grid(row=14, column=2,rowspan=2,columnspan=2, pady=40)
        # l11.config(bg="black", fg="white")
        l11.config(bg="burlywood4", fg="black")


        l5 = Label(window, text="Customer Name", font=myFont)
        l5.grid(row=0, column=0)
        l5.config(bg="burlywood4", fg="black")

        l0 = Label(window, text="Customer ID", font=myFont)
        l0.grid(row=0, column=2, pady=20)
        l0.config(bg="burlywood4", fg="black")

        l1 = Label(window, text="Order ID", font=myFont)
        l1.grid(row=1, column=2, pady=20)
        l1.config(bg="burlywood4", fg="black")

        l2 = Label(window, text="Status", font=myFont)
        l2.grid(row=2, column=2, pady=20)
        l2.config(bg="burlywood4", fg="black")

        l3 = Label(window, text="Due Date", font=myFont)
        l3.grid(row=0, column=4, pady=20, padx=20)
        l3.config(bg="burlywood4", fg="black")

        l4 = Label(window, text="Total Selling Price", font=myFont)
        l4.grid(row=1, column=4, pady=20, padx=20)
        l4.config(bg="burlywood4", fg="black")

        #ayush
        # self.buf = database.get_drop_down()
        # self.cus_list = StringVar(window)
        # self.cus_list.set("List-of-names")
        # self.e6 = OptionMenu(window, self.cus_list, *self.buf, command=self.all_name_ids)
        # self.e6.config(font=myFont)
        # MU = window.nametowidget(self.e6.menuname)
        # MU.config(font=myFont)
        # self.e6.grid(row=0, column=2, pady=20)

        self.cus_name = StringVar()
        # self.cus_name = self.cus_list.get()
        self.e5 = Entry(window, textvariable=self.cus_name, font=myFont)
        self.e5.grid(row=0, column=1, pady=20)
        self.e5.bind('<KeyRelease>', self.partial_text)

        self.cus_id_text = StringVar()
        self.e0 = Entry(window, textvariable=self.cus_id_text, font=myFont)
        self.e0.grid(row=0, column=3,pady=20)
        
        self.order_id_text = StringVar()
        self.e1 = Entry(window, textvariable=self.order_id_text, font=myFont)
        self.e1.grid(row=1, column=3,pady=20)

        self.due_text = StringVar()
        self.e3 = Entry(window, textvariable=self.due_text, font=myFont)
        self.e3.grid(row=0, column=5, pady=20)

        self.selling_text = StringVar()
        self.e4= Entry(window, textvariable=self.selling_text, font=myFont)
        self.e4.grid(row=1, column=5, pady=20)

        self.status_text = StringVar()
        self.e2 = Entry(window, textvariable=self.status_text, font=myFont)
        self.e2.grid(row=2, column=3, pady=20)    

        self.list1 = Listbox(window, height=10, width=70, font=myFont_2)
        self.list1.grid(row=4, column=0, rowspan=5, columnspan=3,padx=20, pady=20)
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        self.list_names = Listbox(window, height=5, width=22,font=myFont_2)
        self.list_names.grid(row=1, column=1, rowspan=2, padx=20)
        self.list_names.bind('<<ListboxSelect>>', self.get_selected_row_names)
        self.partial_text('<KeyRelease>')
        
        # now we need to attach a scrollbar to the listbox, and the other direction,too
        sb1 = Scrollbar(window)
        sb1.grid(row=2, column=3, rowspan=6)
        self.list1.config(yscrollcommand=sb1.set)
        sb1.config(command=self.list1.yview)

        # sb2 = Scrollbar(window)
        # sb2.grid(row=1, column=3)
        # self.list_names.config(yscrollcommand=sb2.set)
        # sb2.config(command=self.list_names.yview)

        b1 = Button(window, text="View all Entries", height = 2, width=12, command=self.view_command, font=myFont)
        b1.grid(row=4, column=4,columnspan=2,padx=20, pady=20)

        b2 = Button(window, text="Search entry", height = 2,width=12, command=self.search_command, font=myFont)
        b2.grid(row=5, column=4,padx=20, pady=20)

        b3 = Button(window, text="Add entry", height = 2,width=12, command=self.add_command, font=myFont)
        b3.grid(row=5, column=5,padx=20, pady=20)

        b4 = Button(window, text="Update selected", height = 2,width=12, command=self.update_command, font=myFont)
        b4.grid(row=6, column=4,padx=20, pady=20)

        b5 = Button(window, text="Delete selected", height = 2,width=12, command=self.delete_command, font=myFont)
        b5.grid(row=6, column=5,padx=20, pady=20)

        b6 = Button(window, text="Close", height = 2,width=12, command=window.destroy, font=myFont)
        b6.grid(row=7, column=4,columnspan=2,padx=20, pady=20)

        b7 = Button(window, text="Clear all Text", height = 2,width=12, command=self.clear_command, font=myFont)
        b7.grid(row=2, column=0,padx=20, pady=20)

        b8 = Button(window, text="Order Line", height = 2,width=12, command=self.order_line_command, font=myFont)
        b8.grid(row=2, column=4, columnspan=2,padx=20, pady=20)


    # def copy(self, event=None):
    #     window.clipboard_clear()
    #     text = self.order_id_text.get()
    #     window.clipboard_append(text)

    def order_line_command(self):
        os.system('python3 order_line.py')
        # cb.copy(self.selected_tuple[1])
        # window.clipboard_clear()
        # window.clipboard_append(self.selected_tuple[1])
        # pyperclip.copy(self.selected_tuple[1])
        window.destroy()

    def clear_command(self):
        self.e0.delete(0,END)
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        self.e5.delete(0,END)
        self.list1.delete(0, END)
        # self.cus_list.set("List-of-names")
        self.list_names.delete(0, END)
        self.partial_text('<KeyRelease>')

    def all_name_ids(self,event):
            self.e5.delete(0,END)
            self.e5.insert(END,self.cus_list.get())
            self.e0.delete(0,END)
            self.e0.insert(END,database.get_id(self.cus_list.get()))
            self.partial_text('<KeyRelease>')

    def partial_text(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            # print(self.e5.get())
            self.list_names.delete(0,END)
            temp_li = database.partial_list_func(self.e5.get())
            for row in temp_li:
                self.list_names.insert(END, row)

        except IndexError:
            pass  

    def get_selected_row_names(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            index = self.list_names.curselection()[0]
            self.selected_tuple = self.list_names.get(index)
            # print(self.selected_tuple)
            self.e5.delete(0,END)
            self.e5.insert(END,self.selected_tuple)  
            self.e0.delete(0,END)
            self.e0.insert(END,database.get_id(self.selected_tuple))
            self.partial_text('<KeyRelease>')

        except IndexError:
            pass                #in the case where the listbox is empty, the code will not execute

    def mod(self,l1):
        # print(l1)
        return l1[9:]

    def get_selected_row(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.e0.delete(0,END)
            self.e0.insert(END,self.mod(self.selected_tuple[0]))  
            self.e1.delete(0,END)
            self.e1.insert(END,self.mod(self.selected_tuple[1]))
            # window.clipboard_clear()
            # window.clipboard_append(self.mod(self.selected_tuple[1]))
            # window.clipboard_update()
            self.e2.delete(0, END)
            self.e2.insert(END,self.mod(self.selected_tuple[2]))
            self.e3.delete(0, END)
            self.e3.insert(END,self.mod(self.selected_tuple[3]))
            self.e4.delete(0, END)
            self.e4.insert(END,self.mod(self.selected_tuple[4]))
            #ayush
            self.e5.delete(0, END)
            self.e5.insert(END,database.get_name(int(self.mod(self.selected_tuple[0]))))
            self.partial_text('<KeyRelease>')
            # self.cus_list.set(database.get_name(int(self.selected_tuple[0])))

        except IndexError:
            pass                #in the case where the listbox is empty, the code will not execute

    def view_command(self):
        self.partial_text('<KeyRelease>')
        self.list1.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
        l=["Cust_Id   Order_Id                  Order_Status                Due_Date         Total Price"]
        self.list1.insert(END, l)
        for row in database.view():
            # line = '{:6d} {:11d} {:17s} {:11s} {:4d}'.format(row[0], row[1], row[2], row[3], row[4])
            loc_row=[]
            for j in row:
                loc_row.append(" "*9+str(j))
            self.list1.insert(END, loc_row)


    def search_command(self):
        self.list1.delete(0, END)
        l=["Cust_Id   Order_Id                  Order_Status                Due_Date         Total Price"]
        self.list1.insert(END, l)
        for row in database.search(self.cus_id_text.get(), self.order_id_text.get(),self.status_text.get(),self.due_text.get(), self.selling_text.get()):
            # self.list1.insert(END, row)
            loc_row=[]
            for j in row:
                loc_row.append(" "*9+str(j))
            self.list1.insert(END, loc_row)

    def add_command(self):
        database.insert(self.cus_id_text.get(), self.order_id_text.get(), self.status_text.get(),self.due_text.get(), self.selling_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.cus_id_text.get(), self.order_id_text.get(),self.status_text.get(),  self.due_text.get(), self.selling_text.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[1])
        self.view_command()

    def update_command(self):
        #be careful for the next line ---> we are updating using the texts in the entries, not the selected tuple
        database.update(self.selected_tuple[1], self.cus_id_text.get(),self.status_text.get(), self.due_text.get(), self.selling_text.get())
        self.view_command()

#ayush
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
Window(window)
app=FullScreenApp(window)

# window.configure(bg='blue')
# from PIL import Image, ImageTk

# IMAGE_PATH = 'bg-masthead.jpg'
# WIDTH, HEIGTH = 1200, 1200

# canvas = Canvas(window, width=WIDTH, height=HEIGTH)
# canvas.grid()

# img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
# canvas.background = img  # Keep a reference in case this code is put in a function.
# bg = canvas.create_image(0, 0, anchor=NW, image=img)

# image = Image.open('bg-masthead.jpg')
# photo_image = ImageTk.PhotoImage(image)
# label = Label(window, image = photo_image)
# label.grid()

# image = Image.open('bg-masthead.jpg')
# C = Canvas(window, bg="blue", height=250, width=300)
# background_image = ImageTk.PhotoImage(image)
# background_label = Label(window, image=background_image)
# background_label.place(x=0, y=0,relwidth=1,relheight=1)
# C.grid(column=0, row=0)
# window.configure(background=background_image)

# import ImageTk

# FILENAME = 'bg-masthead.jpg'
# canvas = Canvas(window, width=200, height=200)
# canvas.grid()
# tk_img = ImageTk.PhotoImage(file = FILENAME)
# canvas.create_image(0, 0, image=tk_img)

window.mainloop()