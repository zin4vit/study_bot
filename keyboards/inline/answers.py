from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


answers_data = CallbackData('answers', 'answer', 'correct', 'level', 'theme')

def make_answers(answers, correct_answer, level, theme):
    answers_kb = InlineKeyboardMarkup(row_width=4)
    for i in range(len(answers)):
        button = InlineKeyboardButton(text=f'{i + 1}', callback_data=answers_data.new(answer=answers[i].id, correct=correct_answer, level=level, theme=theme))
        answers_kb.add(button)
    answers_kb.add(InlineKeyboardButton(text='Отмена', callback_data=answers_data.new(answer='cancel', correct=correct_answer, level=level, theme=theme)))
    return answers_kb
