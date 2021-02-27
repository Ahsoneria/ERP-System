import sqlite3
from tkinter import messagebox
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS `order_line` ( `id` INTEGER, `line_id` INTEGER PRIMARY KEY AUTOINCREMENT, `sku_id` INTEGER, `inven_id` INTEGER, `due` INTEGER, `price` INTEGER )")
        self.conn.commit()

    def insert(self,id,sku_id,inven_id, due, full):
        #the NULL parameter is for the auto-incremented id
        # self.cur.execute("SELECT qavail,rate,margin FROM `inventory` WHERE id = ? ",(inven_id,))
        # vals =self.cur.fetchall()
        # qavail = vals[0][0]
        # rate = vals[0][1]
        # margin =vals[0][2]
        # # print(qavail)
        # print(qavail,rate,margin)
        # due = int(due)
        # qavail =int(qavail)
        # full= int(full)

        # price =0
        # if(due<=qavail):
        #     qavail-=due
        #     full=due
        #     price=float(rate*(100+margin)*due)/100
        #     due=0
        # else:
        #     due-=qavail
        #     full+=qavail
        #     price=float(rate*(100+margin)*qavail)/100
        #     qavail=0

        # due = str(due)
        # qavail =str(qavail)
        # full= str(full)
        # price = str(price)
        # print(price)

        # self.cur.execute("UPDATE `inventory` SET qavail = ?  WHERE id = ? ",(qavail,inven_id))
        self.cur.execute("SELECT * FROM `order_header` WHERE order_id = ? ",(id,))
        vals =self.cur.fetchall()
        if(len(vals)==0):
            messagebox.showerror("Error", "No such Order ID exists")
            return
        print(vals)

        self.cur.execute("INSERT INTO `order_line` VALUES(?,NULL,?,?,?,?,?)", (id,sku_id, -1, due, 0,0))

        self.conn.commit()



    def view(self):
        self.cur.execute("SELECT * FROM `order_line` ")
        rows = self.cur.fetchall()
        return rows

    def search(self, id="", line_id="", sku_id="", inven_id="", due="", full=""):
        self.cur.execute("SELECT * FROM `order_line` WHERE id = ? OR line_id = ? OR sku_id = ? OR inven_id = ? OR due = ? OR full = ?", (id, line_id, sku_id, inven_id, due, full))
        rows = self.cur.fetchall()
        #conn.close()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM `order_line` WHERE line_id = ?", (id,))
        self.conn.commit()
        #conn.close()

    def update(self,id,line_id,sku_id,inven_id, due, full,now):
        # print(id,name,type,phn1,phn2)
        # self.cur.execute("UPDATE `order_line` SET id = ?, sku_id = ?, inven_id = ?, due_qty = ?, fulfilled = ? WHERE line_id = ?", (id, sku_id, inven_id, due, full, line_id))
        # self.conn.commit()
        self.cur.execute("SELECT qavail,rate,margin FROM `inventory` WHERE id = ? ",(inven_id,))
        vals =self.cur.fetchall()
        qavail = vals[0][0]
        rate = vals[0][1]
        margin =vals[0][2]
        # print(qavail)
        print(qavail,rate,margin)
        due = int(due)
        qavail =int(qavail)
        full= int(full)
        now = int(now)

        self.cur.execute("SELECT price FROM `order_line` WHERE line_id = ? ",(line_id,))
        vals =self.cur.fetchall()
        print("ppp",vals)
        price = int(vals[0][0])
        print("price curr- > ",price)
        if(now<=qavail):
            qavail-=now
            due-=now
            full+=now
            price+=float(rate*(100+margin)*now)/100
        else:
            messagebox.showerror("Error", "Quantity not available in inventory")
            return
           
            # due-=qavail
            # full+=qavail
            # price=float(rate*(100+margin)*qavail)/100
            # qavail=0

        due = str(due)
        qavail =str(qavail)
        full= str(full)
        price = str(price)
        print(price)

        self.cur.execute("UPDATE `inventory` SET qavail = ?  WHERE id = ? ",(qavail,inven_id))

        self.cur.execute("SELECT due FROM `account` WHERE order_id = ? ",(id,))
        vals =self.cur.fetchall()
        due_curr = int(vals[0][0])
        self.cur.execute("UPDATE `account` SET due = ?  WHERE order_id = ? ",(due_curr+float(rate*(100+margin)*now)/100,id))
        
        self.cur.execute("UPDATE `order_line` SET id = ?, sku_id = ? , inven_id = ? ,due = ?, full = ? , price =? WHERE line_id =? ", (id,sku_id, inven_id, due, full,price,line_id))
        self.conn.commit()

    #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()
        
# import sqlite3
# from tkinter import messagebox
# class Database:
#     def __init__(self,db):
#         self.conn = sqlite3.connect(db)
#         self.cur = self.conn.cursor()
#         self.cur.execute("CREATE TABLE IF NOT EXISTS `order_line` ( `id` INTEGER, `line_id` INTEGER PRIMARY KEY AUTOINCREMENT, `sku_id` INTEGER, `inven_id` INTEGER, `due` INTEGER, `price` INTEGER )")
#         self.conn.commit()

#     def insert(self,id,sku_id,inven_id, due, full):
#         #the NULL parameter is for the auto-incremented id
#         # self.cur.execute("SELECT qavail,rate,margin FROM `inventory` WHERE id = ? ",(inven_id,))
#         # vals =self.cur.fetchall()
#         # qavail = vals[0][0]
#         # rate = vals[0][1]
#         # margin =vals[0][2]
#         # # print(qavail)
#         # print(qavail,rate,margin)
#         # due = int(due)
#         # qavail =int(qavail)
#         # full= int(full)

#         # price =0
#         # if(due<=qavail):
#         #     qavail-=due
#         #     full=due
#         #     price=float(rate*(100+margin)*due)/100
#         #     due=0
#         # else:
#         #     due-=qavail
#         #     full+=qavail
#         #     price=float(rate*(100+margin)*qavail)/100
#         #     qavail=0

#         # due = str(due)
#         # qavail =str(qavail)
#         # full= str(full)
#         # price = str(price)
#         # print(price)

#         # self.cur.execute("UPDATE `inventory` SET qavail = ?  WHERE id = ? ",(qavail,inven_id))
#         self.cur.execute("SELECT * FROM `order_header` WHERE order_id = ? ",(id,))
#         vals =self.cur.fetchall()
#         if(len(vals)==0):
#             messagebox.showerror("Error", "No such Order ID exists")
#             return
#         print(vals)

#         self.cur.execute("INSERT INTO `order_line` VALUES(?,NULL,?,?,?,?,?)", (id,sku_id, -1, due, 0,0))

#         self.conn.commit()



#     def view(self):
#         self.cur.execute("SELECT * FROM `order_line` ")
#         rows = self.cur.fetchall()
#         return rows

#     def search(self, id="", line_id="", sku_id="", inven_id="", due="", full=""):
#         self.cur.execute("SELECT * FROM `order_line` WHERE id = ? OR line_id = ? OR sku_id = ? OR inven_id = ? OR due = ? OR full = ?", (id, line_id, sku_id, inven_id, due, full))
#         rows = self.cur.fetchall()
#         #conn.close()
#         return rows

#     def delete(self,id):
#         self.cur.execute("DELETE FROM `order_line` WHERE line_id = ?", (id,))
#         self.conn.commit()
#         #conn.close()

#     def update(self,id,line_id,sku_id,inven_id, due, full,now):
#         # print(id,name,type,phn1,phn2)
#         # self.cur.execute("UPDATE `order_line` SET id = ?, sku_id = ?, inven_id = ?, due_qty = ?, fulfilled = ? WHERE line_id = ?", (id, sku_id, inven_id, due, full, line_id))
#         # self.conn.commit()
#         self.cur.execute("SELECT qavail,rate,margin FROM `inventory` WHERE id = ? ",(inven_id,))
#         vals =self.cur.fetchall()
#         qavail = vals[0][0]
#         rate = vals[0][1]
#         margin =vals[0][2]
#         # print(qavail)
#         print(qavail,rate,margin)
#         due = int(due)
#         qavail =int(qavail)
#         full= int(full)
#         now = int(now)

#         self.cur.execute("SELECT price FROM `order_line` WHERE line_id = ? ",(line_id,))
#         vals =self.cur.fetchall()
#         print("ppp",vals)
#         price = int(vals[0][0])
#         print("price curr- > ",price)
#         if(now<=qavail):
#             qavail-=now
#             due-=now
#             full+=now
#             price+=float(rate*(100+margin)*now)/100
#         else:
#             messagebox.showerror("Error", "Quantity not available in inventory")
#             return
           
#             # due-=qavail
#             # full+=qavail
#             # price=float(rate*(100+margin)*qavail)/100
#             # qavail=0

#         due = str(due)
#         qavail =str(qavail)
#         full= str(full)
#         price = str(price)
#         print(price)

#         self.cur.execute("UPDATE `inventory` SET qavail = ?  WHERE id = ? ",(qavail,inven_id))
        
#         self.cur.execute("UPDATE `order_line` SET id = ?, sku_id = ? , inven_id = ? ,due = ?, full = ? , price =? WHERE line_id =? ", (id,sku_id, inven_id, due, full,price,line_id))
#         self.conn.commit()

#     #destructor-->now we close the connection to our database here
#     def __del__(self):
#         self.conn.close()

    def get_name(self, id):
        self.cur.execute("SELECT * FROM `product` WHERE sku_id = ? ", (id,))
        rows = self.cur.fetchall()
        ret = []
        for i in rows:
            ret.append(i[1])
        #conn.close()
        return ret

    def get_id(self, name):
        self.cur.execute("SELECT * FROM `product` WHERE name = ? ", (name,))
        rows = self.cur.fetchall()

        #conn.close()
        return rows[0][0]

    def partial_list_func(self, text):
        self.cur.execute("SELECT * FROM `product` WHERE name LIKE '%{}%' ".format(text))
        rows = self.cur.fetchall()
        ret = []
        for i in rows:
            ret.append(i[1])

        #conn.close()
        return ret

    def get_customer_name_order(self, orderid):
        self.cur.execute("SELECT * FROM `order_header` WHERE order_id = ? ",(orderid,))
        rows = self.cur.fetchall()
        self.cur.execute("SELECT * FROM `customer` WHERE id = ? ", (rows[0][0],))
        ret = self.cur.fetchall()
        #conn.close()
        return ret[0][1]

    def list_orders(self, name):
        self.cur.execute("SELECT * FROM `customer` WHERE name = ? ", (name,))
        rows = self.cur.fetchall()
        ret = []
        # print(rows)
        if rows != []:
            cust_id = rows[0][0]
            self.cur.execute("SELECT * FROM `order_header` WHERE cust_id = ? ", (cust_id,))
            rows = self.cur.fetchall()
            for i in rows:
                ret.append(i[1])
        #conn.close()
        return ret

    def partial_list_cust(self, text):
        self.cur.execute("SELECT * FROM `customer` WHERE name LIKE '%{}%'".format(text))
        rows = self.cur.fetchall()
        ret = []
        for i in rows:
            ret.append(i[1])

        #conn.close()
        return ret

    def inventory_li(self, id):
        self.cur.execute("SELECT * FROM `inventory` WHERE sku_id = ? ", (id,))
        rows = self.cur.fetchall()
        # print(rows)
        ret = []
        # print(rows)
        if rows != []:
            # cust_id = rows[0][0]
            # self.cur.execute("SELECT * FROM `order_header` WHERE cust_id = ? ", (cust_id,))
            # rows = self.cur.fetchall()
            for i in rows:
                ret.append([i[0],i[6]])
        #conn.close()
        return ret