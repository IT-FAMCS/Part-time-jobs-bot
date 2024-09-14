from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

filters=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Город'),KeyboardButton(text='Отрасль'), KeyboardButton(text='Опыт работы')],
    [KeyboardButton(text='Тип занятости'),KeyboardButton(text='График работы')]

], resize_keyboard=True, input_field_placeholder='Filters')

city=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Минск",callback_data='minsk')],
    [InlineKeyboardButton(text="Гомель",callback_data='gomel')],
])

field=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Айти сфера",callback_data='it')],
    [InlineKeyboardButton(text="Кафе, рестораны",callback_data='cafe')],
    [InlineKeyboardButton(text="Репетиторство",callback_data='tutoring')],
])

experience=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="без опыта",callback_data='no_ex')],
    [InlineKeyboardButton(text="От 1 года до 3 лет",callback_data='one_to_three')],
    [InlineKeyboardButton(text="От 3 года до 6 лет",callback_data='three_to_six')],
    [InlineKeyboardButton(text="Более 6 лет",callback_data='from_six')],
])

employment=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Полная",callback_data='full')],
    [InlineKeyboardButton(text="Частичная",callback_data='part_time')],
    [InlineKeyboardButton(text="Стажировка",callback_data='internship')],
])

emp_schedule=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Полный день",callback_data='full_day')],
    [InlineKeyboardButton(text="Сменный график",callback_data='shift')],
    [InlineKeyboardButton(text="Удаленная работа",callback_data='remote_work')],
    [InlineKeyboardButton(text="Гибкий график",callback_data='flexible_sch')],
])
current_situation=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Поиск'),KeyboardButton(text='Фильтры'), KeyboardButton(text='Информация')],
    ], resize_keyboard=True, input_field_placeholder='Filters')
back_to_filters=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Фильтры'),KeyboardButton(text='Поиск')],
    ], resize_keyboard=True, input_field_placeholder='Filters')