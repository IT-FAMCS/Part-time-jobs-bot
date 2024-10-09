from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from functools import partial
import keyboard as kb
router=Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply('Привет!', reply_markup=kb.current_situation)

@router.message(F.text=="Фильтры")
async def start_filters(message:Message):
    await message.answer('Выбери фильтр',reply_markup=kb.filters)
    
@router.message(F.text == "Поиск")
async def cmd_search(message:Message):
    await message.answer("(")

@router.message(F.text=="Информация")
async def info(message:Message):
    
    message_text = (
        f"Текущие фильтры:\n"
        f"ID:\n"
        f"Город:\n"
        f"Образование:\n "
        f"Тип занятости:\n"
        f"Опыт работы:\n "
        f"График работы:\n"
        f"О нашем боте))"
    )
    await message.answer(message_text,reply_markup=kb.back_to_filters)

@router.message(F.text=="Ключевые слова")
async def cmd_key_words(message:Message):
    await message.answer('Настройте ключевые слова',reply_markup=kb.key_words) 

@router.message(F.text=="Добавить ключевое слово")
async def cmd_add_key_words(message:Message):
    async def get_key_words(message:Message):
     words=message.text
     include=words.split(',')
     output='\n'.join(include)
     await message.answer(f"Текущие ключевые слова: \n{output}")
    router.message.register(get_key_words)
    await message.answer('Напишите ключевые слова через запятую',reply_markup=kb.current_situation)

@router.message(F.text=="Добавить слово исключение")
async def cmd_add_key_words(message:Message):
    async def get_key_words(message:Message):
     words=message.text
     exclude=words.split(',')
     output='\n'.join(exclude)
     await message.answer(f"Текущие слова исключения: \n{output}")
    router.message.register(get_key_words)
    await message.answer('Напишите слова исключения через запятую',reply_markup=kb.current_situation) 

@router.message(F.text=="Сброс слов исключений")
async def delete_answer(message:Message):
     await message.answer("Слова успешно удалены")
@router.message(F.text=="Сброс ключевых слов")
async def delete_answer(message:Message):
     await message.answer("Слова успешно удалены")
@router.message(F.text=="Зарплата")
async def start_filters(message:Message):
    await message.answer('Выберите из предложеных вариантов',reply_markup=kb.salary)


@router.callback_query(F.data.in_({"BYN", "USD", "RUR"}))
async def process_callback(callback: CallbackQuery):
        currency=callback.data
        async def check_number(message: Message):
            try:
                number = int(message.text)
                await message.answer(f"Спасибо! Вы ввели значение зарплаты: {number} {currency}")
            except ValueError:
                await message.answer("Это не число. Пожалуйста, введите число:")
        await callback.message.answer('Пожалуйста, введите сумму:')
        router.message.register(check_number)
        await callback.answer()

@router.message(F.text=="Регион")
async def start_filters(message:Message):
    async def get_region(message:Message):
        region=message.text
        await message.answer(f"Спасибо! Вы ввели значение региона: {region}")
    router.message.register(get_region)
    await message.answer("Введите регион:")


@router.message(F.text=="Образование")
async def start_filters(message:Message):
    await message.answer('Выберите из предложеных вариантов',reply_markup=kb.field)
@router.message(F.text=="Опыт работы")
async def start_filters(message:Message):
    await message.answer('Выберите из предложеных вариантов',reply_markup=kb.experience)
@router.message(F.text=="Тип занятости")
async def start_filters(message:Message):
    await message.answer('Выберите из предложеных вариантов',reply_markup=kb.employment)
@router.message(F.text=="График работы")
async def start_filters(message:Message):
    await message.answer('Выберите из предложеных вариантов',reply_markup=kb.schedule)
@router.callback_query()
async def continue_process(callback:CallbackQuery):
    await callback.answer("В разаработке") 