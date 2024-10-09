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