import telebot;

bot = telebot.TeleBot('6456136259:AAElOCKMQPdWSveu67w_4vdOiq1j5dIcgnA')

@bot.message_handler(commands=['start']) #отслеживание определенной команды
def main(massage):  #def это функция
  bot.send_message(massage.chat.id, 'Hellow') #параметра parase_mode='html' позволит писать в сообщение HTML

@bot.message_handler(commands=['info']) #отслеживание определенной команды
def info(massage):
  bot.send_message(massage.chat.id, massage) #вся инфа о чате и пользователи в чавте

bot.polling(non_stop=True) #не прерывность программы
