import sqlite3
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS `login` ( `username` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `password` INTEGER NOT NULL )")
        self.conn.commit()

    def login(self, uname, password):
        self.cur.execute("SELECT * FROM login WHERE username = ? AND password = ?", (uname, password))
        rows = self.cur.fetchall()
        # print(len(rows))
        return len(rows)

    def insert(self,username, password):
        #the NULL parameter is for the auto-incremented username
        self.cur.execute("INSERT INTO login VALUES(NULL,?)", (password))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM login")
        rows = self.cur.fetchall()
        return rows

    def search(self, username="", password=""):
        self.cur.execute("SELECT * FROM login WHERE username = ? OR password = ?", (username ,password))
        rows = self.cur.fetchall()
        #conn.close()
        return rows

    def delete(self,username):
        self.cur.execute("DELETE FROM login WHERE username= ?", (username,))
        self.conn.commit()
        #conn.close()

    def update(self,username, password):
        # print(username,name,type,phn1,phn2)
        self.cur.execute("UPDATE login SET password = ? WHERE username = ?", (password, username))
        self.conn.commit()

    #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()