import sqlite3
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS `employee` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `name` TEXT, `level` INTEGER NOT NULL, `phn1` INTEGER NOT NULL, `phn2` INTEGER NOT NULL )")
        self.conn.commit()

    def insert(self,id, name, level, phn1, phn2):
        #the NULL parameter is for the auto-incremented id
        self.cur.execute("INSERT INTO employee VALUES(NULL,?,?,?,?)", (name,level,phn1,phn2))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM employee")
        rows = self.cur.fetchall()
        return rows

    def search(self, id="", name="", level="", phn1="", phn2=""):
        self.cur.execute("SELECT * FROM employee WHERE id = ? OR name = ? OR level = ? OR phn1 = ? "
                    "OR phn2 = ?", (id ,name, level, phn1, phn2))
        rows = self.cur.fetchall()
        #conn.close()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM employee WHERE id = ?", (id,))
        self.conn.commit()
        #conn.close()

    def update(self,id, name, level, phn1, phn2):
        # print(id,name,level,phn1,phn2)
        self.cur.execute("UPDATE employee SET name = ?, level = ?, phn1 = ?, phn2 = ? WHERE id = ?", (name, level, phn1, phn2, id))
        self.conn.commit()

    #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()
