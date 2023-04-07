from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

level_data = CallbackData('levels', 'level')
choose_level_kb = InlineKeyboardMarkup()
button_seven = InlineKeyboardButton('7 класс', callback_data=level_data.new(level='7'))
button_eight = InlineKeyboardButton('8 класс', callback_data=level_data.new(level='8'))
button_nine = InlineKeyboardButton('9 класс', callback_data=level_data.new(level='9'))
button_ten = InlineKeyboardButton('10 класс', callback_data=level_data.new(level='10'))
button_eleven = InlineKeyboardButton('11 класс', callback_data=level_data.new(level='11'))
button_oge = InlineKeyboardButton('ОГЭ', callback_data=level_data.new(level='огэ'))
button_ege = InlineKeyboardButton('ЕГЭ', callback_data=level_data.new(level='егэ'))
choose_level_kb.row(button_seven, button_eight, button_nine)
choose_level_kb.row(button_ten, button_eleven)
choose_level_kb.row(button_oge, button_ege)
