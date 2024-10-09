from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

filters=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Регион'),KeyboardButton(text='Зарплата'),KeyboardButton(text='Образование'), KeyboardButton(text='Опыт работы')],
    [KeyboardButton(text='Тип занятости'),KeyboardButton(text='График работы'), KeyboardButton(text='Ключевые слова')]

], resize_keyboard=True, input_field_placeholder='Filters')

key_words=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Добавить ключевое слово'), KeyboardButton(text='Добавить слово исключение')]
], resize_keyboard=True, input_field_placeholder='Key_words')

salary=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="BYN",callback_data='BYN')],
    [InlineKeyboardButton(text="USD",callback_data='USD')],
    [InlineKeyboardButton(text="RUR",callback_data='RUR')],
])

field=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Не указано или не требуется",callback_data='not_required_or_not_specified')],
    [InlineKeyboardButton(text="Высшее",callback_data='higher')],
    [InlineKeyboardButton(text="Среднее профессиональное",callback_data='special_secondary')],
])

experience=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="без опыта",callback_data='noExperience')],
    [InlineKeyboardButton(text="От 1 года до 3 лет",callback_data='between1And3')],
    [InlineKeyboardButton(text="От 3 года до 6 лет",callback_data='between3And6')],
    [InlineKeyboardButton(text="Более 6 лет",callback_data='moreThan6')],
])

employment=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Полная занятость",callback_data='full')],
    [InlineKeyboardButton(text="Частичная занятость",callback_data='part')],
    [InlineKeyboardButton(text="Стажировка",callback_data='probation')],
    [InlineKeyboardButton(text="Проектная работа",callback_data='project')],
])

schedule=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Полный день",callback_data='fullDay')],
    [InlineKeyboardButton(text="Сменный график",callback_data='shift')],
    [InlineKeyboardButton(text="Удаленная работа",callback_data='remote')],
    [InlineKeyboardButton(text="Гибкий график",callback_data='flexible')],
    [InlineKeyboardButton(text="Вахтовый метод",callback_data='flyInFlyOut')],
    
])
current_situation=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Сброс слов исключений'),KeyboardButton(text='Сброс ключевых слов'),],
    [KeyboardButton(text='Информация'),KeyboardButton(text='Поиск'),KeyboardButton(text='Фильтры'),]
    ], resize_keyboard=True, input_field_placeholder='Filters')
back_to_filters=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Фильтры'),KeyboardButton(text='Поиск')],
    ], resize_keyboard=True, input_field_placeholder='Filters')