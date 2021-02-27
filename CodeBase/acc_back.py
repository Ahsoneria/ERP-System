import sqlite3
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()        
        self.cur.execute("CREATE TABLE IF NOT EXISTS `account` ( `cust_id` INTEGER, `order_id` INTEGER, `due` INTEGER, `full` INTEGER )")
        self.conn.commit()

    def insert(self,cust_id,order_id,due,full,settle):
        #the NULL parameter is for the auto-incremented id
        self.cur.execute("INSERT INTO `account` VALUES(?,?,?,?,?)", (cust_id,order_id,due,full,settle))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM `account`")
        rows = self.cur.fetchall()
        return rows

    def search(self, cust_id="", order_id="" ) :
        self.cur.execute("SELECT * FROM `account` WHERE order_id = ? OR cust_id = ? ", (order_id ,cust_id))
        rows = self.cur.fetchall()
        #conn.close()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM `account` WHERE order_id = ?", (id,))
        self.conn.commit()
        #conn.close()

    def update(self,cust_id,order_id,due,full,settle):
        # print(id,name,type,phn1,phn2)
        due=int(due)
        full=int(full)
        settle=int(settle)
        full+=settle
        due-=settle

        self.cur.execute("UPDATE `account` SET due=?, full=? WHERE order_id = ?", (str(due),str(full),order_id))
        self.conn.commit()

    #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()


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
        # print(rows)
        if rows != []:
            cust_id = rows[0][0]
            self.cur.execute("SELECT * FROM `order_header` WHERE cust_id = ? ", (cust_id,))
            rows = self.cur.fetchall()
            # print(rows)
            for i in rows:
                ret.append(i[1])
        #conn.close()
        return ret