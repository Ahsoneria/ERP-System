from tkinter import *
from order_line_back import  Database
from tkinter.font import Font
import tkinter.ttk as ttk

database = Database("sap.db")

class Window(object):

    def __init__(self,window):
        self.window = window
        self.window.wm_title("Order Line Screen")

        # window.bind('<Control-v>', self.paste)

        myFont = Font(family="Times New Roman", size=21)
        myFont_2 = Font(family="Times New Roman", size=19)
        myFont_3 = Font(family="Times New Roman", size=23)

        ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=9, columnspan=7, sticky='we')
        ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=10, columnspan=7, sticky='we')
        ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=11, columnspan=7, sticky='we')

        l10 = Label(window, text="Order Line Screen", font=myFont_3)
        l10.grid(row=12, column=2,rowspan=2,columnspan=2, pady=15)
        # l10.config(bg="black", fg="white")
        l10.config(bg="burlywood4", fg="black")

        l11 = Label(window, text="Sai Bhandar", font=myFont_3)
        l11.grid(row=14, column=2,columnspan=2, pady=15)
        # l11.config(bg="black", fg="white")
        l11.config(bg="burlywood4", fg="black")

        l8 = Label(window, text="Customer Name", font=myFont)
        l8.grid(row=0, column=2)
        l8.config(bg="burlywood4", fg="black")

        l7 = Label(window, text="Product Name", font=myFont)
        l7.grid(row=1, column=0)
        l7.config(bg="burlywood4", fg="black")

        l0 = Label(window, text="Order ID", font=myFont)
        l0.grid(row=0, column=4, pady=20)
        l0.config(bg="burlywood4", fg="black")

        l1 = Label(window, text="Line ID", font=myFont)
        l1.grid(row=3, column=4, pady=20)
        l1.config(bg="burlywood4", fg="black")

        l2 = Label(window, text="SKU ID", font=myFont)
        l2.grid(row=0, column=0, pady=20)
        l2.config(bg="burlywood4", fg="black")

        l3 = Label(window, text="Inventory ID", font=myFont)
        l3.grid(row=3, column=2, padx=20,pady=20,)
        l3.config(bg="burlywood4", fg="black")

        l4 = Label(window, text="Total Due Qty.", font=myFont)
        l4.grid(row=4, column=0, padx=20,pady=20)
        l4.config(bg="burlywood4", fg="black")

        l5 = Label(window, text="Total Fulfilled Qty.", font=myFont)
        l5.grid(row=5, column=0, padx=20,pady=20)
        l5.config(bg="burlywood4", fg="black")

        l6 = Label(window, text="Fulfill Now ", font=myFont)
        l6.grid(row=4, column=4, padx=20,pady=20)
        l6.config(bg="burlywood4", fg="black")

        self.cust_text = StringVar()
        self.e8 = Entry(window, textvariable=self.cust_text, font=myFont)
        self.e8.grid(row=0, column=3, pady=20)
        self.e8.bind('<KeyRelease>', self.func1)

        self.prod_name = StringVar()
        # self.cus_name = window.clipboard_get()
        self.e7 = Entry(window, textvariable=self.prod_name, font=myFont)
        self.e7.grid(row=1, column=1)
        self.e7.bind('<KeyRelease>', self.partial_text)

        self.order_id_text = StringVar()
        # self.order_id_text = window.clipboard_get()
        # self.order_id_text = cb.paste()
        self.e0 = Entry(window, textvariable=self.order_id_text, font=myFont)
        self.e0.grid(row=0, column=5, pady=20)

        self.line_id_text = StringVar()
        self.e1 = Entry(window, textvariable=self.line_id_text, font=myFont)
        self.e1.grid(row=3, column=5, pady=20)

        self.sku_text = StringVar()
        self.e2 = Entry(window, textvariable=self.sku_text, font=myFont)
        self.e2.grid(row=0, column=1, pady=20)

        self.inven_text = StringVar()
        self.e3 = Entry(window, textvariable=self.inven_text, font=myFont)
        self.e3.grid(row=3, column=3, pady=20)

        self.due_text = StringVar()
        self.e4= Entry(window, textvariable=self.due_text, font=myFont)
        self.e4.grid(row=4, column=1, pady=20)

        self.fulfilled_text = StringVar()
        self.e5= Entry(window, textvariable=self.fulfilled_text, font=myFont)
        self.e5.grid(row=5, column=1, pady=20)

        self.fulfill_now = StringVar()
        self.e6= Entry(window, textvariable=self.fulfill_now, font=myFont)
        self.e6.grid(row=4, column=5, pady=20)

        self.list1 = Listbox(window, height=8, width=70, font=myFont_2)
        self.list1.grid(row=6, column=0, rowspan=3, columnspan=3, padx=20,pady=20)
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        self.list_names = Listbox(window, height=4, width=22,font=myFont_2)
        self.list_names.grid(row=2, column=1, rowspan=2, padx=20)
        self.list_names.bind('<<ListboxSelect>>', self.get_selected_row_names)
        self.partial_text('<KeyRelease>')

        self.order_names = Listbox(window, height=4, width=22,font=myFont_2)
        self.order_names.grid(row=1, column=5, rowspan=2, padx=20)
        self.order_names.bind('<<ListboxSelect>>', self.get_selected_row_orders)

        self.customer_names = Listbox(window, height=4, width=22,font=myFont_2)
        self.customer_names.grid(row=1, column=3, rowspan=2, padx=20)
        self.customer_names.bind('<<ListboxSelect>>', self.get_selected_customers)
        self.func1('<KeyRelease>')

        self.inventory_names = Listbox(window, height=4, width=22,font=myFont_2)
        self.inventory_names.grid(row=4, column=3, rowspan=2, padx=20)
        self.inventory_names.bind('<<ListboxSelect>>', self.inventory_select)

        # now we need to attach a scrollbar to the listbox, and the other direction,too
        sb1 = Scrollbar(window)
        sb1.grid(row=5, column=3, rowspan=3)
        self.list1.config(yscrollcommand=sb1.set)
        sb1.config(command=self.list1.yview)

        b1 = Button(window, text="View all",height = 2, width=12, command=self.view_command, font=myFont)
        b1.grid(row=5, column=4, columnspan=2,padx=20, pady=20)

        b2 = Button(window, text="Search entry", height = 2,width=12, command=self.search_command, font=myFont)
        b2.grid(row=6, column=4,padx=20, pady=20)

        b3 = Button(window, text="Add entry", height = 2,width=12, command=self.add_command, font=myFont)
        b3.grid(row=6, column=5,padx=20, pady=20)

        b4 = Button(window, text="Update selected", height = 2,width=12, command=self.update_command, font=myFont)
        b4.grid(row=7, column=4,padx=20, pady=20)

        b5 = Button(window, text="Delete selected", height = 2,width=12, command=self.delete_command, font=myFont)
        b5.grid(row=7, column=5,padx=20, pady=20)

        b6 = Button(window, text="Close", height = 2,width=12, command=window.destroy, font=myFont)
        b6.grid(row=12, column=4, columnspan=2,padx=20, pady=20)

        b7 = Button(window, text="Clear all Text", height = 2,width=12, command=self.clear_command, font=myFont)
        b7.grid(row=3, column=0,padx=20, pady=20)


    # def logout(self):
    #     window.destroy()
    #     os.system('python3 login.py')
    # def paste(self, event=None):
    #     text = window.selection_get(selection='CLIPBOARD')
    #     self.e0.insert('insert', text)

    def inventory_select(self, event):
        try:
            index = self.inventory_names.curselection()[0]
            self.selected_tuple = self.inventory_names.get(index)

            self.e3.delete(0,END)
            self.e3.insert(END,self.selected_tuple[0])  

        except IndexError:
            pass 

    def inventory_list(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            # print(self.e2.get())
            self.inventory_names.delete(0,END)
            self.e3.delete(0,END)
            temp_li = database.inventory_li(self.e2.get())
            # temp_li=temp_li[::-1]
            # print(temp_li)
            for row in temp_li:
                self.inventory_names.insert(END, row)

        except IndexError:
            pass


    def get_selected_row_orders(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            index = self.order_names.curselection()[0]
            self.selected_tuple = self.order_names.get(index)
            # print(self.selected_tuple)
            self.e0.delete(0,END)
            self.e0.insert(END,self.selected_tuple)  
            # self.e8.delete(0,END)
            # self.e8.insert(END,database.get_customer_name_order(self.selected_tuple))

        except IndexError:
            pass 

    def get_selected_customers(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            index = self.customer_names.curselection()[0]
            self.selected_tuple = self.customer_names.get(index)
            # print(self.selected_tuple)
            self.e8.delete(0,END)
            self.e8.insert(END,self.selected_tuple)  
            self.corresponding_orders('<KeyRelease>')

        except IndexError:
            pass 

    def func1(self,event):
        # print(self.e5.get())
            self.customer_names.delete(0,END)
            temp_li = database.partial_list_cust(self.e8.get())
            for row in temp_li:
                self.customer_names.insert(END, row)

    def corresponding_orders(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            self.order_names.delete(0,END)
            self.e0.delete(0,END)
            temp_li = database.list_orders(self.e8.get())
            temp_li=temp_li[::-1]
            # print(temp_li)
            for row in temp_li:
                self.order_names.insert(END, row)

        except IndexError:
            pass

    def clear_command(self):
        self.e0.delete(0,END)
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        self.e5.delete(0,END)
        self.e6.delete(0,END)
        self.e7.delete(0,END)
        self.e8.delete(0,END)
        self.list1.delete(0, END)
        # self.cus_list.set("List-of-names")
        self.list_names.delete(0, END)
        self.order_names.delete(0,END)
        self.customer_names.delete(0,END)
        self.inventory_names.delete(0,END)
        self.partial_text('<KeyRelease>')
        self.func1('<KeyRelease>')

    # def all_name_ids(self,event):
    #         self.e7.delete(0,END)
    #         self.e7.insert(END,self.cus_list.get())
    #         self.e2.delete(0,END)
    #         self.e2.insert(END,database.get_id(self.cus_list.get()))
    #         self.partial_text('<KeyRelease>')

    def partial_text(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            # print(self.e5.get())
            self.list_names.delete(0,END)
            temp_li = database.partial_list_func(self.e7.get())
            for row in temp_li:
                self.list_names.insert(END, row)

        except IndexError:
            pass 

    def get_selected_row_names(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            index = self.list_names.curselection()[0]
            self.selected_tuple = self.list_names.get(index)
            # print(self.selected_tuple)
            self.e7.delete(0,END)
            self.e7.insert(END,self.selected_tuple)  
            self.e2.delete(0,END)
            self.e2.insert(END,database.get_id(self.selected_tuple))
            self.partial_text('<KeyRelease>')
            self.inventory_list('<KeyRelease>')

        except IndexError:
            pass 
        
    def mod(self,l1):
        # print(l1)
        return int(l1[12:])

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
            self.e4.delete(0, END)
            self.e4.insert(END,self.mod(self.selected_tuple[4]))
            self.e5.delete(0, END)
            self.e5.insert(END,self.mod(self.selected_tuple[5]))

            self.e7.delete(0, END)
            self.e7.insert(END,database.get_name(int(self.selected_tuple[2])))
            self.partial_text('<KeyRelease>')

            self.order_names.delete(0,END)
            self.customer_names.delete(0,END)
            self.inventory_names.delete(0,END)

            self.e8.delete(0, END)
            self.e8.insert(END,database.get_customer_name_order(self.selected_tuple[0]))

        except IndexError:
            pass                #in the case where the listbox is empty, the code will not execute


    def view_command(self):
        # self.customer_names.delete(0,END)
        self.partial_text('<KeyRelease>')
        self.list1.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
        l=["Order_Id       Line_Id      SKU_Id    Inven_Id   Due_Amt   Fullfilled     Total Price"]
        self.list1.insert(END, l)
        for row in database.view():
            # print(row)
            loc_row=[]
            for j in row:
                loc_row.append(" "*12 +str(j))
            # print(loc_row)
            self.list1.insert(END, loc_row)

    def search_command(self):
        self.list1.delete(0, END)
        l=["Order_Id       Line_Id      SKU_Id    Inven_Id   Due_Amt   Fullfilled     Total Price"]
        self.list1.insert(END, l)
        for row in database.search(self.order_id_text.get(), self.sku_text.get(), self.due_text.get(), self.line_id_text.get(), self.inven_text.get(), self.fulfilled_text.get()):
            # self.list1.insert(END, row)
            # print(row)
            loc_row=[]
            for j in row:
                loc_row.append(" "*12 +str(j))
            # print(loc_row)
            self.list1.insert(END, loc_row)

    def add_command(self):
        database.insert(self.order_id_text.get(), self.sku_text.get(), self.inven_text.get(), self.due_text.get(), self.fulfilled_text.get())
        self.list1.delete(0, END)
        # self.list1.insert(END, (self.order_id_text.get(), self.sku_text.get(), self.inven_text.get(), self.due_text.get(), self.fulfilled_text.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[1])
        self.view_command()

    def update_command(self):
        #be careful for the next line ---> we are updating using the texts in the entries, not the selected tuple
        database.update(self.selected_tuple[0], self.selected_tuple[1], self.sku_text.get() ,self.inven_text.get(),self.due_text.get(), self.fulfilled_text.get(),self.fulfill_now.get())
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
# window.configure(bg=0x008080)
window.mainloop()