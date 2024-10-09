import sqlite3 as sql
from scrapper import Scrap


#https://hh.ru/search/vacancy?L_save_area=true&text=aaaa&excluded_text=aaaaaa&area=1002&salary=123124&currency_code=RUR&education=not_required_or_not_specified&experience=between1And3&employment=full&schedule=fullDay&part_time=employment_project&label=with_address&order_by=relevance&search_period=0&items_on_page=50&hhtmFrom=vacancy_search_filter
class SQLConnect():
    def __init__(self):
        self.scrap = Scrap()
        self.connect = sql.connection('base/db.sqlite3', check_same_thread=False)
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TINYTEXT, include TEXT, exclude TEXT, region INTEGER, salary INTEGER, experience TEXT, education TEXT, employment TEXT, schedule TEXT, part_time TEXT)")
    def register_user(self, username):
        include = ''
        exclude = ''
        region = 0
        salary = 0
        experience = '' 
        education = '' 
        employment = ''
        schedule = '' 
        part_time = '' 
        if self.cursor.execute("SELECT username FROM users WHERE username = ?", (username,)).fetchone() is not None:            
            pass           
        else:
            self.cursor.execute("INSERT INTO users (username, include, exclude, region, salary, experience, education, employment, schedule, part_time, ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,)", (username, include, exclude, region, salary, experience, education, employment, schedule, part_time, ))
            self.connect.commit()
    def get_filters(self, username):
        try:
            temp = self.cursor.execute("SELECT include, exclude, region, salary, experience, education, employment, schedule, part_time, FROM users WHERE username = ?", (username))
            return temp.fetchall()
        except sql.Error as e:
            return {'error at getting filters': e}
    def add_filters(self, username, include, exclude, region, salary, experience, education, employment, schedule, part_time):
        try:
            self.cursor.execute("UPDATE users SET include = ?, exclude = ?, region = ?, salary = ?, experience = ?, education = ?, employment = ?, schedule = ?, part_time = ? WHERE username = ?", (include, exclude, region, salary, experience, education, employment, schedule, part_time, username))
            self.connect.commit()
            return True
        except sql.Error as e:
            return {'error at adding filters': e}
    def generate_link(self, **kwargs):
        pass
    def search(self, username):
        filters = self.get_filters(username)
        url = self.generate_link(filters)
        self.scrap.add_url(url)
        vacancies = self.scrap.parse()
        return vacancies
    def generate_message(self, vacancies):
        for vacancy in vacancies:
            pass