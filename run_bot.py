#!/usr/bin/env python
from __future__ import print_function
import os
import sys
import argparse
import yaml
import logging
import logging.config
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

#logging section
logger = logging.getLogger(__name__)
log_config_file = "D:/DATA/Company/Werkmap/Scripting/Python/bot_test/log/logging.yaml"
with open(log_config_file, 'r') as f:
    log_config = yaml.safe_load(f.read())
logging.config.dictConfig(log_config)


def msg():
    """ usage """
    return ("{0}".format(os.path.basename(sys.argv[0])))+'''
        [-h, --help     show howto invoke and possible arguments]
        [-b, --bot_id   use valid bot_id]
        
        example:
        1) run_bot.py -b <use valid bot_id>

        '''
#Arguments section
parser = argparse.ArgumentParser(description='Run Bot Updater for given bot_id', usage=msg())
parser.add_argument('-b', '--bot_id',
                    required=True,
                    help="use valid bot_id")
args = parser.parse_args()


def start(bot, update):
    test_msg = "Hi {0}, I am a bot!".format(update.message.from_user.first_name)
    bot.send_message(chat_id=update.message.chat_id, text=test_msg)

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def main():
    updater = Updater(token=args.bot_id)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
