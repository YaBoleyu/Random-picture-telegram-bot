from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import random
import os

path = "PATH"

# Random picture function 
def init(bot, update):
    directory = path
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
