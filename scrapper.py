import bs4
import selenium
import sqlite3 as sql

class SQLConnect():
    def __init__(self):
        self.connect = sql.connection('base/db.sqlite3', check_same_thread=False)
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id SMALLINT PRIMARY KEY AUTOINCREMENT, username TINYTEXT, include TEXT, exclude TEXT, )")
    def register_user(self, username):
        include = ''
        exclude = ''
        if self.cursor.execute("SELECT username FROM users WHERE username = ?", (username,)).fetchone() is not None:            
            pass           
        else:
            self.cursor.execute("INSERT INTO users (username, include, exclude) VALUES (?, ?, ?)", (username, include, exclude))
            self.connect.commit()
    def get_filters(self, username):
        temp = self.cursor.execute("SELECT include, exclude FROM users WHERE username = ?", (username))
        return temp.fetchall()
    def search(self, username):
        filters = self.get_filters(username)
        
