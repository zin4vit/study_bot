from loader import dp
from aiogram.types import Message, CallbackQuery
from db.models import *
from loader import session, admin
import matplotlib.pyplot as plt
import os
import random
from keyboards.inline.admin import *
import asyncio
from utils.stickers import *
import csv



@dp.message_handler()
async def admin_start(message: Message):
    if str(message.from_user.id) == admin:
        await message.answer('Управление ботом.\nВыберите действие:', reply_markup=adminstart_kb)
    else:
        await message.answer('Извините, это меню администратора.\nВы не являетесь администратором')


@dp.callback_query_handler(admin_start_data.filter())
async def menu(callback: CallbackQuery, callback_data: dict):
    if callback_data['action'] == 'show_users':
        users_list = session.query(User).all()
        with open('users.csv', 'w') as file:
            writer = csv.writer(file)
            for user in users_list:
                writer.writerow((
                    user.id,
                    user.tg_id,
                    user.username,
                    user.name,
                    user.last_dt
                ))
        await callback.message.answer_document(open('users.csv', 'rb'), caption='Пользователи')
        os.remove('users.csv')

