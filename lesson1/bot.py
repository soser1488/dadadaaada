import ephem
import time
from ephem import (Body, Planet, Moon, Jupiter, Saturn, PlanetMoon,
                   Date, Observer, readtle, readdb,
                   FixedBody, EllipticalBody, HyperbolicBody,
                   ParabolicBody, EarthSatellite,
                   constellation)
from datetime import date, timedelta, datetime


import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import set

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
def start_bot(bot, update):
    mytext = "Привет {}! Я выполняю только команду {}".format(update.message.chat.first_name, '/start')
    update.message.reply_text(mytext)



def chat(bot, update):
    text = "{}, пошел ты нахер козел!!!!!!".format(update.message.chat.first_name)
    logging.info(text)
    update.message.reply_text(text)

def posilaet(bot, update):
    text1 = "{}, иди ты нахуй, а!".format(update.message.chat.first_name)
    logging.info(text1)
    update.message.reply_text(text1)


def poka(bot, update):
    text2 = "Пока {}, буду скучать, приходи еще".format(update.message.chat.first_name)
    logging.info(text2)
    update.message.reply_text(text2)

def privet(bot, update):
    text3 = "Привет, рад тебя снова видеть))"
    logging.info(text3)
    update.message.reply_text(text3)

def creator(bot, update):
    text4 = """Меня написал Никита Мракобесов
vk: https://vk.com/joj1337
telegram: @soser1488"""
    logging.info(text4)
    update.message.reply_text(text4)

def wpikaloff(bot, update):
    text4 = """Андрей, ты дурак?
ТЕБЕ НЕЛЬЗЯ ПОТАНЦЕВАТЬ"""
    logging.info(text4)
    update.message.reply_text(text4)


def planet_search(bot,update):
    planets=['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
    user_input_cap=update.message.text[8:].capitalize()
    print('поиск планеты')
    print('планета, которую ввел пользователь', user_input_cap)
    for index in planets:
        print(index)
        if user_input_cap==index:
            d=datetime.now().strftime('%Y')
            if user_input_cap=='Sun':
                planet_answer=ephem.constellation(ephem.Sun(datetime.now().strftime('%Y')))[1]
                update.message.reply_text(planet_answer) 
                print(planet_answer)
            elif user_input_cap=='Moon':
                planet_answer=ephem.constellation(ephem.Moon(datetime.now().strftime('%Y')))[1]
                update.message.reply_text(planet_answer)   
                print(planet_answer)
            elif user_input_cap=='Mercury':
                planet_answer=ephem.constellation(ephem.Mercury(datetime.now().strftime('%Y')))[1]
                update.message.reply_text(planet_answer) 
                print(planet_answer) 
            elif user_input_cap=='Venus':
                planet_answer=ephem.constellation(ephem.Venus(datetime.now().strftime('%Y')))[1]
                update.message.reply_text(planet_answer)  
                print(planet_answer)
            elif user_input_cap=='Mars':
                planet_answer=ephem.constellation(ephem.Mars(datetime.now().strftime('%Y')))[1]
                update.message.reply_text(planet_answer)  
                print(planet_answer) 
            elif user_input_cap=='Jupiter':
                planet_answer=ephem.constellation(ephem.Jupiter(datetime.now().strftime('%Y')))[1]
                print(planet_answer) 
                update.message.reply_text(planet_answer)
                print(len(user_input_cap))    
            elif user_input_cap=='Saturn':
                planet_answer=ephem.constellation(ephem.Saturn(datetime.now().strftime('%Y')))[1]
                update.message.reply_text(planet_answer)  
                print(planet_answer)
            elif user_input_cap=='Uranus':
                planet_answer=ephem.constellation(ephem.Uranus(datetime.now().strftime('%Y')))[1]
                update.message.reply_text(planet_answer) 
                print(planet_answer) 
            elif user_input_cap=='Neptune':
                planet_answer=ephem.constellation(ephem.Neptune(datetime.now().strftime('%Y')))[1]
                update.message.reply_text(planet_answer) 
                print(planet_answer) 
            elif user_input_cap=='Pluto':
                planet_answer=ephem.constellation(ephem.Pluto(datetime.now().strftime('%Y')))[1]
                update.message.reply_text(planet_answer)
                print(planet_answer)
def wordcount(bot, update):
    user_input=update.message.text[11:].capitalize()
    
    abd = len(user_input.split())
    if abd == 0:
        update.message.reply_text("Нет слов")
    elif abd > 1:
        update.message.reply_text("{} Слово".format(abd))
    elif abd <= 4:
        update.message.reply_text("{} Слова".format(abd))
    if abd <= 5:
        update.message.reply_text("{} Слов".format(abd))




def calcul(bot, update):
    userinput=update.message.text[8:].capitalize()

    jopa = userinput.split( )
    try:
        if len(jopa) < 2:
            update.message.reply_text("Вы не ввели числа/о или знак")
        else:
            if jopa[1] == "*":
                res = int(jopa[0]) * int(jopa[2])
            elif jopa[1] == "+":
                res = int(jopa[0]) + int(jopa[2])
            elif jopa[1] == "-":
                res = int(jopa[0]) - int(jopa[2])
            elif jopa[1] == "/":
                try:
                    res = int(jopa[0]) / int(jopa[2])
                except ZeroDivisionError:
                    update.message.reply_text("На 0 делить нельзя!!!!!")
    except (ValueError, IndexError):
        update.message.reply_text("Введите числа, а не буквы")            
    update.message.reply_text(res)

def main():
    upd = Updater(set.TELEGRAM_API_KEY)
    upd.dispatcher.add_handler(CommandHandler("wordcount", wordcount))
    upd.dispatcher.add_handler(CommandHandler("planet", planet_search))
    upd.dispatcher.add_handler(CommandHandler("calcul", calcul))
    upd.dispatcher.add_handler(CommandHandler("wpikaloff", wpikaloff))
    upd.dispatcher.add_handler(CommandHandler("creator", creator))
    upd.dispatcher.add_handler(CommandHandler("posil", posilaet))
    upd.dispatcher.add_handler(CommandHandler("poka", poka))
    upd.dispatcher.add_handler(CommandHandler("privet", privet))
    upd.dispatcher.add_handler(CommandHandler("start", start_bot))
    upd.dispatcher.add_handler(MessageHandler(Filters.text, chat))
    upd.start_polling()
    upd.idle()



if __name__=="__main__":
    logging.info('Bot started')
    main()