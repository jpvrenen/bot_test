#!/usr/bin/env python
import time
import sys
import xmltodict

from tools.connect import Connect

def main():
    con_ripe = Connect(  host='rest.db.ripe.net' )
    print(con_ripe.get_as('213.133.47.254'))


if __name__ == "__main__":
    main()
