import sqlite3
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS `customer` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `name` TEXT, `type` INTEGER NOT NULL, `phn1` INTEGER NOT NULL, `phn2` INTxEGER NOT NULL )")
        self.conn.commit()

    def insert(self,id, name, type, phn1, phn2):
        #the NULL parameter is for the auto-incremented id
        self.cur.execute("INSERT INTO customer VALUES(NULL,?,?,?,?)", (name,type,phn1,phn2))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM customer")
        rows = self.cur.fetchall()
        return rows

    def search(self, id="", name="", type="", phn1="", phn2=""):
        self.cur.execute("SELECT * FROM customer WHERE id = ? OR name = ? OR type = ? OR phn1 = ? "
                    "OR phn2 = ?", (id ,name, type, phn1, phn2))
        rows = self.cur.fetchall()
        #conn.close()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM customer WHERE id = ?", (id,))
        self.conn.commit()
        #conn.close()

    def update(self,id, name, type, phn1, phn2):
        # print(id,name,type,phn1,phn2)
        self.cur.execute("UPDATE customer SET name = ?, type = ?, phn1 = ?, phn2 = ? WHERE id = ?", (name, type, phn1, phn2, id))
        self.conn.commit()

    #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()

    def get_drop_down(self):
        self.cur.execute("SELECT * FROM customer")
        rows = self.cur.fetchall()
        ret = []
        for i in rows:
            ret.append(i[1])
        #conn.close()
        return ret