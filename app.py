from aiogram import executor
from loader import dp, bot
import handlers
from utils.set_bot_commands import set_default_commands
from config import *



async def on_startup(dp):
    await set_default_commands(dp)






if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)
