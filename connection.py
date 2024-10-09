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
    def generate_link(self, filters) -> str:
        base_url = "https://hh.ru/search/vacancy?"
        params = {
            "text": filters[0],          
            "excluded_text": filters[1],  
            "area": filters[2],           
            "salary": filters[3],         
            "experience": filters[4],     
            "education": filters[5],      
            "employment": filters[6],     
            "schedule": filters[7],       
            "part_time": filters[8],     
            "L_save_area": "true",        
            "order_by": "relevance",      
            "items_on_page": 50          
        }
        
        query_string = "&".join([f"{key}={value}" for key, value in params.items() if value])
        result_url = base_url + query_string
        return result_url
    def truncate_string(input_string: str, word_limit=50) -> str:
        words = input_string.split()  
        if len(words) > word_limit:
            truncated = " ".join(words[:word_limit]) + "..."  
            return truncated
        return input_string 
    def search(self, username) -> list:
        filters = self.get_filters(username)
        url = self.generate_link(filters)
        self.scrap.add_url(url)
        vacancies = self.scrap.parse()
        return vacancies
    def generate_message(self, vacancies) -> list:
        for iteration in range(3):
            vacancies_messages = f"""<b>{vacancies[0].pop(iteration)}</b>
            <p>{self.truncate_string(vacancies[1].pop(iteration))}</p>
            <p>ЗП: {vacancies[2].pop(iteration)}</p>
            """
            urls = vacancies[3].pop(iteration)
        return (vacancies_messages, urls)

        