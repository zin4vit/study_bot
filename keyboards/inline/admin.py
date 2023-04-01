from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


admin_start_data = CallbackData('start', 'action')
adminstart_kb = InlineKeyboardMarkup()
adminstart_kb.add(InlineKeyboardButton('Посмотреть пользователей', callback_data=admin_start_data.new(action='show_users')))