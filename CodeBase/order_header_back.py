import sqlite3
from tkinter import messagebox

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS `order_header` ( `cust_id` INTEGER, `order_id` INTEGER, `status` TEXT, `date` TEXT, `tsp` INTEGER, PRIMARY KEY(`order_id`) )")
        self.conn.commit()

    def insert(self,cust_id,order_id,status,date,tsp):
        #the NULL parameter is for the auto-incremented id

        self.cur.execute("SELECT * FROM `customer` WHERE id = ? ",(cust_id,))
        vals =self.cur.fetchall()
        if(len(vals)==0):
            messagebox.showerror("Error", "No such customer ID exists")
            return
        print(vals)

        self.cur.execute("INSERT INTO `order_header` VALUES(?,NULL,?,?,?)", (cust_id,"ORDER PENDING",date,0))
        self.cur.execute("SELECT last_insert_rowid()")
        vals =self.cur.fetchall()
        print(vals[0][0])
        self.cur.execute("INSERT INTO `account` VALUES(?,?,?,?)", (cust_id,vals[0][0],0,0))
        self.conn.commit()
        

    def view(self):
        self.cur.execute("SELECT * FROM `order_header` ")
        rows = self.cur.fetchall()
        return rows

    def search(self, cust_id="", order_id="", status="", date="", tsp=""):
        self.cur.execute("SELECT * FROM `order_header` WHERE cust_id = ? OR order_id = ? OR status = ? OR date = ? OR tsp = ? ", (cust_id,order_id,status,date,tsp))
        rows = self.cur.fetchall()
        #conn.close()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM `order_header` WHERE order_id = ?", (id,))
        self.conn.commit()
        #conn.close()

    def update(self,order_id,cust_id,status,date,tsp):
        # print(id,name,type,phn1,phn2)
        self.cur.execute("SELECT price FROM `order_line` WHERE id = ? ",(order_id,))
        vals =self.cur.fetchall()
        print(vals)
        tsp=0
        for i in vals:
            tsp+=int(i[0])
        self.cur.execute("SELECT due FROM `order_line` WHERE id = ? ",(order_id,))  
        vals =self.cur.fetchall()
        st=1

        for i in vals:
            if(int(i[0])!=0):
                st = 0
        if(st==0):
            status="ORDER PENDING"
        else:
            status="ORDER COMPLETED"
        
        self.cur.execute("UPDATE `order_header` SET cust_id = ?, status = ?, date= ?, tsp= ? WHERE order_id = ?", (cust_id,status,date,tsp, order_id))
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
#         self.cur.execute("CREATE TABLE IF NOT EXISTS `order_header` ( `cust_id` INTEGER, `order_id` INTEGER, `status` TEXT, `date` TEXT, `tsp` INTEGER, PRIMARY KEY(`order_id`) )")
#         self.conn.commit()

#     def insert(self,cust_id,order_id,status,date,tsp):
#         #the NULL parameter is for the auto-incremented id

#         self.cur.execute("SELECT * FROM `customer` WHERE id = ? ",(cust_id,))
#         vals =self.cur.fetchall()
#         if(len(vals)==0):
#             messagebox.showerror("Error", "No such customer ID exists")
#             return
#         print(vals)

#         # self.cur.execute("SELECT price FROM `order_line` WHERE id = ? ",(order_id,))
#         # vals =self.cur.fetchall()
#         # tsp=0
#         # for i in vals:
#         #     tsp+=int(i[0])
#         # self.cur.execute("SELECT due FROM `order_line` WHERE id = ? ",(order_id,))  
#         # vals =self.cur.fetchall()
#         # st=1

#         # for i in vals:
#         #     if(int(i[0])!=0):
#         #         st = 0
#         # if(st==0):
#         #     status="ORDER PENDING"
#         # else:
#         #     status="ORDER COMPLETED"

#         # self.cur.execute("UPDATE `inventory` SET qavail = ?  WHERE id = ? ",(qavail,inven_id))
        

#         self.cur.execute("INSERT INTO `order_header` VALUES(?,NULL,?,?,?)", (cust_id,"ORDER PENDING",date,0))
#         self.conn.commit()



#     def view(self):
#         self.cur.execute("SELECT * FROM `order_header` ")
#         rows = self.cur.fetchall()
#         return rows

#     def search(self, cust_id="", order_id="", status="", date="", tsp=""):
#         self.cur.execute("SELECT * FROM `order_header` WHERE cust_id = ? OR order_id = ? OR status = ? OR date = ? OR tsp = ? ", (cust_id,order_id,status,date,tsp))
#         rows = self.cur.fetchall()
#         #conn.close()
#         return rows

#     def delete(self,id):
#         self.cur.execute("DELETE FROM `order_header` WHERE order_id = ?", (id,))
#         self.conn.commit()
#         #conn.close()

#     def update(self,order_id,cust_id,status,date,tsp):
#         # print(id,name,type,phn1,phn2)
#         self.cur.execute("SELECT price FROM `order_line` WHERE id = ? ",(order_id,))
#         vals =self.cur.fetchall()
#         print(vals)
#         tsp=0
#         for i in vals:
#             tsp+=int(i[0])
#         self.cur.execute("SELECT due FROM `order_line` WHERE id = ? ",(order_id,))  
#         vals =self.cur.fetchall()
#         st=1

#         for i in vals:
#             if(int(i[0])!=0):
#                 st = 0
#         if(st==0):
#             status="ORDER PENDING"
#         else:
#             status="ORDER COMPLETED"
        
#         self.cur.execute("UPDATE `order_header` SET cust_id = ?, status = ?, date= ?, tsp= ? WHERE order_id = ?", (cust_id,status,date,tsp, order_id))
#         self.conn.commit()

#     #destructor-->now we close the connection to our database here
#     def __del__(self):
#         self.conn.close()

    #ayush
    def get_drop_down(self):
        self.cur.execute("SELECT * FROM `customer`")
        rows = self.cur.fetchall()
        ret = []
        for i in rows:
            ret.append(i[1])
        #conn.close()
        return ret

    def get_name(self, id):
        self.cur.execute("SELECT * FROM `customer` WHERE id = ?", (id,))
        rows = self.cur.fetchall()
        ret = []
        for i in rows:
            ret.append(i[1])
        #conn.close()
        return ret

    def get_id(self, name):
        self.cur.execute("SELECT * FROM `customer` WHERE name = ?", (name,))
        rows = self.cur.fetchall()

        #conn.close()
        return rows[0][0]

    def partial_list_func(self, text):
        self.cur.execute("SELECT * FROM `customer` WHERE name LIKE '%{}%'".format(text))
        rows = self.cur.fetchall()
        ret = []
        for i in rows:
            ret.append(i[1])

        #conn.close()
        return ret