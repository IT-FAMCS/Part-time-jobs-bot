from bs4 import BeautifulSoup
import lxml

# На странице поиска вакансий
# data-sentry-element="MagritteLink" - ссылка на вакансию
# На странице вакансии
# data-sentry-source-file="VacancyTitleRedesigned.tsx" - название вакансии
# data-qa="vacancy-description" - описание вакансии 
# data-qa="vacancy-salary-compensation-type-gross" - зп по вакансии

from bs4 import BeautifulSoup

def clear_data(data: list) -> list:
    """
    Очищает HTML-теги из списка строк.

    Параметры:
    data (list): Список строк, содержащий HTML-теги.

    Возвращает:
    list: Список строк без HTML-тегов.
    """
    cleaned_data = []
    for item in data:
        if isinstance(item, str):  
            soup = BeautifulSoup(item, 'html.parser')
            cleaned_item = soup.get_text()  
            cleaned_data.append(cleaned_item)
        else:
            cleaned_data.append(item)  
    return cleaned_data
            
            
class Scrap():
    def __init__(self):
        """
        Инициализирует экземпляр класса Scrap.
        """
        pass
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
    def add_url(self, url: str):
        """
        Добавляет URL в экземпляр Scrap.

        Параметры:
        url (str): URL для добавления.
        """
        self.start = BeautifulSoup(url, 'lxml.parser')

    def parse(self) -> list:
        """
        Парсит HTML-содержимое добавленного URL и извлекает данные о вакансиях.

        Возвращает:
        list: Список, содержащий названия вакансий, описания, зарплаты и URL-адреса.
        """
        titles = []
        descriptions = []
        salary = []
        data_set = [] 
        urls = clear_data(self.start.find_all('data-sentry-element="MagritteLink"'))
        for i in urls:
            self.scrap = BeautifulSoup(i, 'lxml')
            titles.append(clear_data(self.scrap.find_all('data-sentry-source-file="VacancyTitleRedesigned.tsx"')))
            descriptions.append(clear_data(self.scrap.find_all('data-qa="vacancy-description"')))
            salary.append(clear_data(self.scrap.find_all('data-qa="vacancy-salary-compensation-type-gross"')))
        data_set.append(titles)
        data_set.append(descriptions)
        data_set.append(salary)
        data_set.append(urls)
        return data_set