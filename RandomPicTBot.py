from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import random
import os
import tg_analytic

path = "PATH"


def init(bot, update):
    directory = path
    random_image = random.choice(os.listdir(directory))
    bot.send_photo(update.message.chat_id, photo=open(
        directory + random_image, 'rb'))


def Desktop(bot, update):
    directory = "PATH"
    random_image = random.choice(os.listdir(directory))
    bot.send_photo(update.message.chat_id, photo=open(
        directory + random_image, 'rb'))


def main():
    updater = Updater('TOKEN')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('pic', init))
    dp.add_handler(CommandHandler('dsk', Desktop))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
