from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


theme_data = CallbackData('themes', 'theme', 'level')
def make_themes(level):
    choose_theme_kb = InlineKeyboardMarkup()
    button_quantity_symbol = InlineKeyboardButton('Обозначения', callback_data=theme_data.new(theme='symbol', level=level))
    button_quantity_unit = InlineKeyboardButton('Единицы измерения', callback_data=theme_data.new(theme='unit', level=level))
    button_quantity_equation = InlineKeyboardButton('Формулы', callback_data=theme_data.new(theme='equation', level=level))
    choose_theme_kb.add(button_quantity_symbol)
    choose_theme_kb.add(button_quantity_unit)
    choose_theme_kb.add(button_quantity_equation)
    choose_theme_kb.add(InlineKeyboardButton(text='Отмена', callback_data=theme_data.new(theme='cancel', level=level)))
    return choose_theme_kb