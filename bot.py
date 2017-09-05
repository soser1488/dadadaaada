import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import set

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
def start_bot(bot, update):
    mytext = "Привет {}! Я выполняю только команду {}".format(update.message.chat.first_name, '/start')
    logging.info('Пользователь {} нажал /start'.format(update.message.chat.username))
    update.message.reply_text(mytext)
def chat(bot, update):
    text = update.message.text
    logging.info(text)
    update.message.reply_text(text)

def main():
    upd = Updater(set.TELEGRAM_API_KEY)

    upd.dispatcher.add_handler(CommandHandler("start", start_bot))
    upd.dispatcher.add_handler(MessageHandler(Filters.text, chat))
    upd.start_polling()
    upd.idle()


if __name__=="__main__":
    logging.info('Bot started')
    main()