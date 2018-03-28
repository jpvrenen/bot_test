#!/usr/bin/env python
import json

from collections import OrderedDict
from requests import Request, Session, codes

s = Session()

def do_request(req):
    result = dict()
    result['headers_rec'] = dict()
    result['data_rec'] = str()
    result['rfs'] = bool() #raise for status
    prepped = req.prepare()
    try:
        r = s.send( prepped,
                    verify=False)
        result['headers_rec'] = r.headers
        result['data_rec'] = r.text
        #status_code = r.status_code
        result['rfs'] = r.raise_for_status() #None for all is OK
    except Exception as e:
        print("do_request: {0}".format(e))
        result['rfs'] = True #Oeps something went wrong

    return result

def telegram_get_me(host, bot):
    headers_generic={'Accept' : 'application/json'}
    url_query = "https://{0}/bot{1}/getMe".format(host, bot)
    req = Request('GET', url_query, headers=headers_generic)
    req_result = do_request(req)
    return req_result

def telegram_get_updates(host, bot):
    headers_generic={'Accept' : 'application/json'}
    url_query = "https://{0}/bot{1}/getUpdates".format(host, bot)
    req = Request('GET', url_query, headers=headers_generic)
    req_result = do_request(req)
    return req_result


class Connect(object):
    """Create connect class"""

    def __init__(self, **kwargs):
        self.host = 'api.telegram.org'
        self.bot = kwargs['bot_id']

    def get_me(self):
        return telegram_get_me(self.host, self.bot)

    def get_updates(self):
        return telegram_get_updates(self.host, self.bot)
