from loader import dp
from aiogram.types import Message, CallbackQuery
from db.models import *
from loader import session
import matplotlib.pyplot as plt
import os
import random
from keyboards.inline.answers import *
from keyboards.inline.levels import *
from keyboards.inline.themes import *
import asyncio
from utils.stickers import *

async def make_png(items, user_id):
    text_list = []
    for i in range(len(items)):
        f = rf'${i + 1}.\ {items[i]}$'
        text_list.append(f)
    text = '\n'.join(text_list)

    ### Создание области отрисовки
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()

    ### Отрисовка формулы
    t = ax.text(0.1, 0.5, text,
                horizontalalignment='left',
                verticalalignment='center',
                fontsize=10, color='black')

    ### Определение размеров формулы
    ax.figure.canvas.draw()
    bbox = t.get_window_extent()

    # Установка размеров области отрисовки
    fig.set_size_inches(bbox.width / 80, bbox.height / 80)  # dpi=80

    ### Отрисовка или сохранение формулы в файл
    # plt.show()
    plt.savefig(f'{user_id}_task.png', dpi=300)

@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer('Hello friend!')
    await message.answer_sticker('CAACAgIAAxkBAAEIUm5kHzuo6ObjBhj2AAHV-x9nH9ygqEAAAu3KAAJji0YMdRUN2BcLG3UvBA')
    await choose_level(message=message)


@dp.message_handler(commands=['test'])
async def choose_level(message: Message):
    await message.answer('Выберите уровень', reply_markup=choose_level_kb)
    await message.answer_sticker('CAACAgIAAxkBAAEIUnxkHzyKGcAGkH7YkfDcRsWHO7hPewACagYAAoA_Byg5XCsozc2JFS8E')



@dp.callback_query_handler(theme_data.filter(theme='cancel'))
@dp.callback_query_handler(level_data.filter(level='cancel'))
@dp.callback_query_handler(answers_data.filter(answer='cancel'))
async def cancel(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Выберите уровень', reply_markup=choose_level_kb)
    await callback.message.answer_sticker('CAACAgIAAxkBAAEIUnxkHzyKGcAGkH7YkfDcRsWHO7hPewACagYAAoA_Byg5XCsozc2JFS8E')

@dp.callback_query_handler(level_data.filter())
async def choose_theme(callback: CallbackQuery, callback_data: CallbackData):
    await callback.message.delete()
    level = callback_data['level']
    await callback.message.answer_sticker('CAACAgIAAxkBAAEIUptkH0T84u4PDQcezDgZpcgHlntgRAACJyMAAmOLRgxSiT5GQp3b9S8E')
    await callback.message.answer('Что будем изучать?', reply_markup=make_themes(level))


@dp.callback_query_handler(theme_data.filter(theme='symbol'))
async def symbol(callback: CallbackQuery, callback_data: CallbackData):
    await callback.message.delete()
    theme = callback_data['theme']
    level = callback_data['level']
    symbols = []
    symbols.append(random.choice(session.query(Symbol).filter(Symbol.level == level).all()))
    while len(symbols) < 4:
        a = random.choice(session.query(Symbol).filter(Symbol.level == level).all())
        for item in symbols:
            if a.symbol == item.symbol or a.name == item.name:
                break
        else:
            symbols.append(a)
    question = random.choice(symbols)
    render_list = []
    for item in symbols:
        render_list.append(item.symbol)
    await make_png(render_list, callback.message.chat.id)
    await callback.message.answer_photo(photo=open(f'{callback.message.chat.id}_task.png', 'rb'),
                                        caption=f'Выберите обозначение для физической величины \n"<b>{question.name.capitalize()}</b>"',
                                        reply_markup=make_answers(symbols, question.id, level, theme))
    os.remove(f'{callback.message.chat.id}_task.png')


@dp.callback_query_handler(theme_data.filter(theme='unit'))
async def unit(callback: CallbackQuery, callback_data: CallbackData):
    await callback.message.delete()
    theme = callback_data['theme']
    level = callback_data['level']
    units = []
    units.append(random.choice(session.query(Unit).filter(Unit.level == level).all()))
    while len(units) < 4:
        a = random.choice(session.query(Unit).filter(Unit.level == level).all())
        for item in units:
            if a.name == item.name or a.unit == item.unit:
                break
        else:
            units.append(a)
    question = random.choice(units)
    render_list = []
    for item in units:
        render_list.append(item.unit)
    await make_png(render_list, callback.message.chat.id)
    await callback.message.answer_photo(photo=open(f'{callback.message.chat.id}_task.png', 'rb'), caption=f'Выберите единицы измерения для физической величины \n"<b>{question.name.capitalize()}</b>"',reply_markup=make_answers(units, question.id, level, theme))
    os.remove(f'{callback.message.chat.id}_task.png')


@dp.callback_query_handler(theme_data.filter(theme='equation'))
async def equation(callback: CallbackQuery, callback_data: CallbackData):
    await callback.message.delete()
    theme = callback_data['theme']
    level = callback_data['level']
    equations = []
    equations.append(random.choice(session.query(Equation).filter(Equation.level == level).all()))
    while len(equations) < 4:
        a = random.choice(session.query(Equation).filter(Equation.level == level).all())
        for item in equations:
            if a.name == item.name or a.equation == item.equation:
                break
        else:
            equations.append(a)
    question = random.choice(equations)
    render_list = []
    for item in equations:
        render_list.append(item.equation)
    await make_png(render_list, callback.message.chat.id)
    await callback.message.answer_photo(photo=open(f'{callback.message.chat.id}_task.png', 'rb'), caption=f'Выберите формулу. \n"<b>{question.name.capitalize()}</b>"',reply_markup=make_answers(equations, question.id, level, theme))
    os.remove(f'{callback.message.chat.id}_task.png')


@dp.callback_query_handler(answers_data.filter(theme='symbol'))
async def check_unit(callback: CallbackQuery, callback_data: CallbackData):
    if callback_data['answer'] == callback_data['correct']:
        try:
            sticker = random.choice(correct_stickers)
            reaction = await callback.message.answer_sticker(sticker)
            await asyncio.sleep(2)
            await reaction.delete()
        except:
            await callback.answer('Правильно!')
        await symbol(callback, callback_data)
    else:
        try:
            sticker = random.choice(incorrect_stickers)
            reaction = await callback.message.answer_sticker(sticker)
            await asyncio.sleep(2)
            await reaction.delete()
        except:
            await callback.answer('Попробуйте ещё раз')


@dp.callback_query_handler(answers_data.filter(theme='unit'))
async def check_unit(callback: CallbackQuery, callback_data: CallbackData):
    if callback_data['answer'] == callback_data['correct']:
        try:
            sticker = random.choice(correct_stickers)
            reaction = await callback.message.answer_sticker(sticker)
            await asyncio.sleep(2)
            await reaction.delete()
        except:
            await callback.answer('Правильно!')
        await unit(callback, callback_data)
    else:
        try:
            sticker = random.choice(incorrect_stickers)
            reaction = await callback.message.answer_sticker(sticker)
            await asyncio.sleep(2)
            await reaction.delete()
        except:
            await callback.answer('Попробуйте ещё раз')


@dp.callback_query_handler(answers_data.filter(theme='equation'))
async def check_equation(callback: CallbackQuery, callback_data: CallbackData):
    if callback_data['answer'] == callback_data['correct']:
        try:
            sticker = random.choice(correct_stickers)
            reaction = await callback.message.answer_sticker(sticker)
            await asyncio.sleep(1.5)
            await reaction.delete()
        except:
            await callback.answer('Правильно!')
        await equation(callback, callback_data)
    else:
        try:
            sticker = random.choice(incorrect_stickers)
            reaction = await callback.message.answer_sticker(sticker)
            await asyncio.sleep(2)
            await reaction.delete()
        except:
            await callback.answer('Попробуйте ещё раз')






