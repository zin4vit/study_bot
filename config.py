import os
from dotenv import load_dotenv

load_dotenv()
bot_token = str(os.getenv('BOT_TOKEN'))
admin = os.getenv('ADMIN')