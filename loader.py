from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from config import bot_token, admin
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


bot = Bot(token=bot_token, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot=bot)


engine = create_engine("sqlite:///db/db.db")
Session = sessionmaker(bind=engine)
session = Session()

from db.models import *

Base.metadata.create_all(engine)




