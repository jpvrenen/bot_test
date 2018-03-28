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
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def main():
    updater = Updater(token=args.bot_id)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
