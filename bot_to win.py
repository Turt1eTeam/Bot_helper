import telebot 
import config_to_win as cf

print('TOKEN:',cf.TOKEN)
print('...BOT started to @Testrt_Pintester_Creator_Bot...')
bot = telebot.TeleBot(cf.TOKEN)
first = False
go_to_win=" 🔥🔥🔥 Горящие задачи: 🔥🔥🔥 \n\nЗадание №1:\nОпределить победителя HACKATHON AUTHUMN 2022.\nОставшееся время: 30 минут.\n\nЗадание №2:\nПоучаствовать в фотосесии.\nОставшееся время: 30 минут."
#go_to_win=" 👾👾👾 Основные задачи: 👾👾👾 \n\n1.Поучаствовать в HACKATHON AUTHUMN 2022;\nОставшееся время: 30 минут;\n\n2.Поучаствовать в фотосесии;\nОставшееся время: 30 минут;"
def event(message):
    pass


@bot.message_handler(commands=['start'])
def event(message):
    bot.send_message(message.chat.id,go_to_win)
       



bot.polling(non_stop=True)