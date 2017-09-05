import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
def start_bot(bot, update):
    mytext = "Привет {}! Я выполняю только команду {}".format(update.message.chat.first_name, '/start')

    update.message.reply_text(mytext)
def chat(bot, update):
    text = update.message.text
    logging.info(text)
    update.message.reply_text(text)

def main():
    upd = Updater('271327454:AAH6mcGzr8i8Zdj30aQi92iTmPnzH0Ut2AU')

    upd.dispatcher.add_handler(CommandHandler("start", start_bot))
    upd.dispatcher.add_handler(MessageHandler(Filters.text, chat))
    upd.start_polling()
    upd.idle()


if __name__=="__main__":
    logging.info('Bot started')
    main()