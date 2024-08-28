import telebot
from telebot import types
import time
from datetime import datetime


now = datetime.now()


TOKEN = ''


CHAT_ID = '@username'

bot = telebot.TeleBot(TOKEN)

def set_chat_description(token, chat_id):
    try:
        c = bot.get_chat_members_count(CHAT_ID)
        time_now= now.strftime('%Y-%m-%d %H:%M')
        bot.set_chat_description(chat_id, f"""
Shaxsiy IT-Blogga xush kelibsiz!

instagram.com/ulugbekweb
youtube.com/ulugbekweb

                                 
📊 Yaqinlarim: {c} ta    
📅 Hozir: {time_now}                       

☎️ Murojat: @admin                               
                                                               
©️ ulugbekweb.uz
""")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")





if __name__ == "__main__":
    while True:
        set_chat_description(TOKEN, CHAT_ID)
        time.sleep(60)
