import telebot;

bot = telebot.TeleBot('6456136259:AAElOCKMQPdWSveu67w_4vdOiq1j5dIcgnA')

@bot.message_handler(commands=['start']) #отслеживание определенной команды
def main(massage):  #def это функция
  bot.send_message(massage.chat.id, 'Hellow') #параметра parase_mode='html' позволит писать в сообщение HTML

@bot.message_handler(commands=['info'])
def info(massage):
  bot.send_message(massage.chat.id, massage) #вся инфа о чате и пользователи в чавте

@bot.message_handler(commands=['faq']) 
def info(massage):
  bot.send_message(massage.chat.id, 'инфа о проекте',parse_mode="html") 

@bot.message_handler()
def info(message):
  if message.text.lower() =="старт":
      bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}') #параметра parase_mode='html' позволит писать в сообщение HTML


bot.polling(non_stop=True) #не прерывность программы
