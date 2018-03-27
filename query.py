#!/usr/bin/env python
from tools.connect import Connect

dolle_bot = '575831428:AAEgSGfiw_s2otNbtEJHF_-JTyag0uMPaso'

def main():
    con_telegram = Connect(  bot_id=dolle_bot )
    print(con_telegram.get_me())


if __name__ == "__main__":
    main()
