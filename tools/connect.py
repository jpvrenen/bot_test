#!/usr/bin/env python
import sys
import re
import base64
import time
import xmltodict
import pprint
import collections
from requests import Request, Session, codes

s = Session()

def do_request(req):
    headers = dict()
    text = str()
    prepped = req.prepare()
    try:
        r = s.send( prepped,
                    verify=False)
        headers = r.headers
        text = r.text
        #status_code = r.status_code
        raise_for_status = r.raise_for_status() #None for all is OK
    except Exception as e:
        print("do_request: {0}".format(e))
        raise_for_status = True #Oeps something went wrong

    return headers,text,raise_for_status

def ripe_get_as(host, query):
    payload = {'query-string': query}
    headers_generic={'Accept' : 'application/xml'}
    url_query = "https://rest.db.ripe.net/search?"
    req = Request('GET', url_query, headers=headers_generic, params=payload)
    headers_received, text_received, raise_for_status = do_request(req)

    return text_received

class Connect(object):
    """Create connect class"""

    def __init__(self, **kwargs):
        self.host = kwargs['host']

    def get_as(self, query):
        return ripe_get_as(self.host, query)
