from tkinter import *
from acc_back import  Database
from tkinter.font import Font
import tkinter.ttk as ttk 
database = Database("sap.db")

class Window(object):
    def __init__(self,window):
        self.window = window
        self.window.wm_title("Accounts Screen")
        myFont = Font(family="Times New Roman", size=21)
        myFont_2 = Font(family="Times New Roman", size=19)
        myFont_3 = Font(family="Times New Roman", size=23)

        ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=7, columnspan=7, sticky='we')
        ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=8, columnspan=7, sticky='we')
        ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=9, columnspan=7, sticky='we')

        l10 = Label(window, text="Accounts Screen", font=myFont_3)
        l10.grid(row=10, column=2,rowspan=2,columnspan=2, pady=40)
        l10.config(bg="burlywood4", fg="black")
        # l10.config(bg="black", fg="white")

        l11 = Label(window, text="Sai Bhandar", font=myFont_3)
        l11.grid(row=12, column=2,rowspan=2,columnspan=2, pady=40)
        l11.config(bg="burlywood4", fg="black")
        # l11.config(bg="black", fg="white")

        l5 = Label(window, text="Customer Name", font=myFont)
        l5.grid(row=0, column=0)
        l5.config(bg="burlywood4", fg="black")

        l0 = Label(window, text="Customer ID", font=myFont)
        l0.grid(row=3, column=0,pady=20)
        l0.config(bg="burlywood4", fg="black")

        l1 = Label(window, text="Order ID", font=myFont)
        l1.grid(row=0, column=4,pady=20)
        l1.config(bg="burlywood4", fg="black")

        l2 = Label(window, text="Total Due Amount", font=myFont)
        l2.grid(row=0, column=2,pady=20)
        l2.config(bg="burlywood4", fg="black")

        l3 = Label(window, text="Total Paid Amount ", font=myFont)
        l3.grid(row=1, column=2,pady=20)
        l3.config(bg="burlywood4", fg="black")

        l4 = Label(window, text="Settle Now Amount ", font=myFont)
        l4.grid(row=2, column=2,pady=20)
        l4.config(bg="burlywood4", fg="black")

        self.cus_name = StringVar()
        # self.cus_name = self.cus_list.get()
        self.e5 = Entry(window, textvariable=self.cus_name, font=myFont)
        self.e5.grid(row=0, column=1, pady=20)
        self.e5.bind('<KeyRelease>', self.partial_text)

        self.cust_id_text = StringVar()
        self.e0 = Entry(window, textvariable=self.cust_id_text, font=myFont)
        self.e0.grid(row=3, column=1,pady=20)

        self.order_id_text = StringVar()
        self.e1 = Entry(window, textvariable=self.order_id_text, font=myFont)
        self.e1.grid(row=0, column=5,pady=20)

        self.due_text = StringVar()
        self.e2 = Entry(window, textvariable=self.due_text, font=myFont)
        self.e2.grid(row=0, column=3,pady=20)

        self.paid_text = StringVar()
        self.e3 = Entry(window, textvariable=self.paid_text, font=myFont)
        self.e3.grid(row=1, column=3,pady=20)

        self.settle_text = StringVar()
        self.e4 = Entry(window, textvariable=self.settle_text, font=myFont)
        self.e4.grid(row=2, column=3,pady=20)

        self.list1 = Listbox(window, height=10, width=70, font=myFont_2)
        self.list1.grid(row=4, column=0, rowspan=4, columnspan=3,padx=20, pady=20)
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        self.list_names = Listbox(window, height=5, width=22,font=myFont_2)
        self.list_names.grid(row=1, column=1, rowspan=2, padx=20)
        self.list_names.bind('<<ListboxSelect>>', self.get_selected_row_names)
        self.partial_text('<KeyRelease>')

        self.order_names = Listbox(window, height=4, width=22,font=myFont_2)
        self.order_names.grid(row=1, column=5, rowspan=2, padx=20)
        self.order_names.bind('<<ListboxSelect>>', self.get_selected_row_orders)

        # now we need to attach a scrollbar to the listbox, and the other direction,too
        sb1 = Scrollbar(window)
        sb1.grid(row=3, column=3, rowspan=6)
        self.list1.config(yscrollcommand=sb1.set)
        sb1.config(command=self.list1.yview)

        b1 = Button(window, text="View all entries", height = 2,width=12, command=self.view_command, font=myFont)
        b1.grid(row=4, column=4,columnspan=2,padx=20, pady=20)

        b2 = Button(window, text="Search entry", height = 2,width=12, command=self.search_command, font=myFont)
        b2.grid(row=5, column=4,padx=20, pady=20)

        b3 = Button(window, text="Add entry", height = 2,width=12, command=self.add_command, font=myFont)
        b3.grid(row=5, column=5,padx=20, pady=20)

        b4 = Button(window, text="Update selected", height = 2,width=12, command=self.update_command, font=myFont)
        b4.grid(row=6, column=4, columnspan=2,padx=20, pady=20)

        # b5 = Button(window, text="Delete selected", height = 2,width=12, command=self.delete_command, font=myFont)
        # b5.grid(row=5, column=5,padx=20, pady=20)

        b6 = Button(window, text="Close", height = 2,width=12, command=window.destroy, font=myFont)
        b6.grid(row=10, column=4,columnspan=2,padx=20, pady=20)

        b7 = Button(window, text="Clear all Text", height = 2,width=12, command=self.clear_command, font=myFont)
        b7.grid(row=3, column=4,columnspan=2,padx=20, pady=20)


    def partial_text(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            # print(self.e5.get())
            self.list_names.delete(0,END)
            temp_li = database.partial_list_func(self.e5.get())
            for row in temp_li:
                self.list_names.insert(END, row)

        except IndexError:
            pass  

    def corresponding_orders(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            self.order_names.delete(0,END)
            self.e1.delete(0,END)
            # print(self.e5.get())
            temp_li = database.list_orders(self.e5.get())
            temp_li=temp_li[::-1]
            # print(temp_li)
            for row in temp_li:
                self.order_names.insert(END, row)

        except IndexError:
            pass

    def get_selected_row_orders(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            index = self.order_names.curselection()[0]
            self.selected_tuple = self.order_names.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple)  

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
            self.corresponding_orders('<KeyRelease>')

        except IndexError:
            pass                #in the case where the listbox is empty, the code will not execute


    def clear_command(self):
        self.e0.delete(0,END)
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        self.e5.delete(0,END)
        self.list1.delete(0, END)
        self.list_names.delete(0, END)
        self.order_names.delete(0, END)
        self.partial_text('<KeyRelease>')

    def mod(self,l1):
        # print(l1)
        return l1[12:]


    def get_selected_row(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.e0.delete(0,END)
            self.e0.insert(END,self.mod(self.selected_tuple[0]))  
            self.e1.delete(0,END)
            self.e1.insert(END,self.mod(self.selected_tuple[1]))
            self.e2.delete(0, END)
            self.e2.insert(END,self.mod(self.selected_tuple[2]))
            self.e3.delete(0, END)
            self.e3.insert(END,self.mod(self.selected_tuple[3]))
            # self.e4.delete(0, END)
            # self.e4.insert(END,self.selected_tuple[4])
            self.e5.delete(0, END)
            self.e5.insert(END,database.get_name(int(self.mod(self.selected_tuple[0]))))
            self.list_names.delete(0, END)
            self.order_names.delete(0, END)
            self.partial_text('<KeyRelease>')
        except IndexError:
            pass                #in the case where the listbox is empty, the code will not execute

    def view_command(self):
        self.list1.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
        #  self.list1.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
        l=["Cust_Id      Order_Id    Due Amount    Paid Amount"]
        self.list1.insert(END, l)
        for row in database.view():
            loc_row=[]
            for j in row:
                loc_row.append(" "*12+str(j))
            self.list1.insert(END, loc_row)

    def search_command(self):
        self.list1.delete(0, END)
        l=["Cust_Id   Order_Id    Due Amount    Paid Amount"]
        self.list1.insert(END, l)
        for row in database.search(self.cust_id_text.get(),self.order_id_text.get(),):
            loc_row=[]
            for j in row:
                loc_row.append(" "*12+str(j))
            self.list1.insert(END, loc_row)
            # self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.cust_id_text.get(), self.order_id_text.get(), self.due_text.get(), self.paid_text.get(), self.settle_text.get())
        self.list1.delete(0, END)
        # self.list1.insert(END, (self.order_id_text.get(), self.sku_text.get(), self.inven_text.get(), self.due_text.get(), self.fulfilled_text.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[1])
        self.view_command()

    def update_command(self):
        #be careful for the next line ---> we are updating using the texts in the entries, not the selected tuple
        database.update(self.selected_tuple[0], self.selected_tuple[1], self.due_text.get() ,self.paid_text.get(),self.settle_text.get())
        self.view_command()

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
# window.config(bg='black')
window.mainloop()