from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

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
        f"Отрасль:\n "
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
    await message.answer('Напишите ключевое слово, ',reply_markup=kb.current_situation)

@router.message(F.text=="Добавить слово исключение")
async def cmd_add_key_words(message:Message):
    await message.answer('Напишите слово исключение',reply_markup=kb.current_situation)         

@router.message(F.text=="Город")
async def start_filters(message:Message):
    await message.answer('Выберите из предложеных вариантов',reply_markup=kb.city)

@router.message(F.text=="Отрасль")
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
    await message.answer('Выберите из предложеных вариантов',reply_markup=kb.emp_schedule)
@router.callback_query()
async def continue_process(callback:CallbackQuery):
    await callback.answer("В разаработке")
    await callback.message.answer("Нажмите ПОИСК если вы закончили добавлять фильтры\n ФИЛЬТРЫ если вы хотите добавить еще фильтров\n ИНФОРМАЦИЯ чтобы посмотреть текущие фильтры", reply_markup=kb.current_situation)