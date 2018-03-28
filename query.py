#!/usr/bin/env python
from __future__ import print_function
import os
import sys
import argparse
from tools.connect import Connect

def msg():
    """ usage """
    return ("{0}".format(os.path.basename(sys.argv[0])))+'''
        [-h, --help     show howto invoke and possible arguments]
        [-b, --bot_id   use valid bot_id]
        
        example:
        1) query.py -b <use valid bot_id>

        '''

#Arguments section
parser = argparse.ArgumentParser(description='Query bot', usage=msg())
parser.add_argument('-b', '--bot_id',
                    required=True,
                    help="use valid bot_id")
args = parser.parse_args()


def main():
    con_telegram = Connect(  bot_id=args.bot_id )
    print(con_telegram.get_me())


if __name__ == "__main__":
    main()
