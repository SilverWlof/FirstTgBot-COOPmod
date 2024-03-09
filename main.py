import TelegramBotAPI;

bot = TelegramBotAPI.telebot('6971566102:AAHPDZSravLVp2g7E4tAsMiXJMl5zeTIZNc')

@bot.message_handler(commands=['start'])
def start (message):
    bot.send_message(message.chat.id, 'Дароу', parse_mode='html')

bot.polling(none_stop=True)

