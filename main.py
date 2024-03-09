import telebot;

bot = telebot.TeleBot('6456136259:AAElOCKMQPdWSveu67w_4vdOiq1j5dIcgnA')

@bot.message_handler(commands=['start']) #отслеживание определенной команды
def main(massage):  #def это функция
  bot.send_message(massage.chat.id, 'Hellow')

bot.polling(non_stop=True) #не прерывность программы