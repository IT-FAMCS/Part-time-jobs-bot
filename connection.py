import sqlite3 as sql
from scrapper import Scrap


class SQLConnect:
    """
    Класс SQLConnect отвечает за управление данными пользователей и взаимодействие с базой данных SQLite.
    Он также включает методы для создания ссылки поиска на основе фильтров пользователей и парсинга данных вакансий.
    """

    def __init__(self):
        """
        Инициализирует класс SQLConnect, создавая подключение к базе данных SQLite и инициализируя класс Scrap.
        """
        self.scrap = Scrap()
        self.connect = sql.connect('base/db.sqlite3', check_same_thread=False)
        self.cursor = self.connect.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TINYTEXT,
                include TEXT,
                exclude TEXT,
                region INTEGER,
                salary INTEGER,
                experience TEXT,
                education TEXT,
                employment TEXT,
                schedule TEXT,
                part_time TEXT
            )
        """)

    def register_user(self, username):
        """
        Регистрирует нового пользователя в базе данных. Если пользователь уже существует, ничего не делает.
        """
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
            self.cursor.execute("""
                INSERT INTO users (username, include, exclude, region, salary, experience, education, employment, schedule, part_time) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (username, include, exclude, region, salary, experience, education, employment, schedule, part_time, ))
            self.connect.commit()

    def get_filters(self, username):
        """
        Возвращает фильтры пользователя из базы данных.
        Возвращает список кортежей или словарь с ошибкой, если возникла ошибка.
        """
        try:
            temp = self.cursor.execute("SELECT include, exclude, region, salary, experience, education, employment, schedule, part_time FROM users WHERE username = ?", (username,))
            return temp.fetchall()
        except sql.Error as e:
            return {'ошибка при получении фильтров': e}

    def add_filters(self, username, include, exclude, region, salary, experience, education, employment, schedule, part_time):
        """
        Обновляет фильтры пользователя в базе данных.
        Возвращает True, если операция выполнена успешно, и словарь с ошибкой, если возникла ошибка.
        """
        try:
            self.cursor.execute("""
                UPDATE users SET include = ?, exclude = ?, region = ?, salary = ?, experience = ?, education = ?, employment = ?, schedule = ?, part_time = ? 
                WHERE username = ?
            """, (include, exclude, region, salary, experience, education, employment, schedule, part_time, username))
            self.connect.commit()
            return True
        except sql.Error as e:
            return {'ошибка при добавлении фильтров': e}

    def generate_link(self, filters) -> str:
        """
        Создает ссылку поиска на сайте HH.ru на основе предоставленных фильтров.
        Возвращает сформированную ссылку в виде строки.
        """
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
        """
        Обрезает входную строку до указанного количества слов.
        Если количество слов во входной строке превышает лимит, обрезает ее и добавляет многоточие.
        Возвращает обрезанную строку.
        """
        words = input_string.split()  
        if len(words) > word_limit:
            truncated = " ".join(words[:word_limit]) + "..."  
            return truncated
        return input_string 

    def search(self, username) -> list:
        """
        Выполняет поиск вакансий на сайте HH.ru на основе фильтров пользователя.
        Возвращает список найденных вакансий.
        """
        filters = self.get_filters(username)
        url = self.generate_link(filters)
        self.scrap.add_url(url)
        vacancies = self.scrap.parse()
        return vacancies

    def generate_message(self, vacancies) -> list:
        """
        Формирует сообщение о вакансии для отправки пользователю.
        Возвращает кортеж из сообщения о вакансии и URL вакансии.
        """
        vacancies_messages = []
        urls = []
        for iteration in range(3):
            vacancies_messages.append(f"""
                <b>{vacancies[0].pop(iteration)}</b>
                <p>{self.truncate_string(vacancies[1].pop(iteration))}</p>
                <p>ЗП: {vacancies[2].pop(iteration)}</p>
            """)
            urls.append(vacancies[3].pop(iteration))
        return (vacancies_messages, urls)