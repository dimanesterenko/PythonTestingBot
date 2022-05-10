import telebot
from telebot import types
bot = telebot.TeleBot('5234420253:AAGRFC-WMifsPVDH-9S1L7QYlGbmFPY6EVM')
@bot.message_handler(commands = ['start'])
def start(message):
    mess = f'Hello,<b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id,mess,parse_mode='html')

# @bot.message_handler() #for any text that user inputs
# def get_user_text(message):
#     if message.text =="привет":
#         bot.send_message(message.chat.id, 'Hey! Matka Boska! ', parse_mode='html')
#     elif message.text == "имя":
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f'Your ID:{message.from_user.id}', parse_mode='html')
#     elif message.text == "username":
#         bot.send_message(message.chat.id, f'Your username:{message.from_user.username}', parse_mode='html')
#     elif message.text == "photo":
#         photo =open("it700.jpg",'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, "I don't understand you!")

@bot.message_handler(content_types = ['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Hey!\nCool photo photo')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()#built in messages any things
    markup.add(types.InlineKeyboardButton("Instagram of developer", url="https://www.instagram.com/_dimanesterenko_/"))
    bot.send_message(message.chat.id, 'Click on insta', reply_markup=markup)

#creating menu with buttons
@bot.message_handler(commands=['menu'])
def menucka(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    info = types.KeyboardButton('Info')
    starting = types.KeyboardButton('Starting')
    markup.add(info, starting)
    bot.send_message(message.chat.id, 'Click on', reply_markup=markup)

bot.polling (none_stop = True)


