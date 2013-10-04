from config import properties

import rethinkdb as r
import json
import sys

r.connect(properties.get('RETHINK_HOST'), properties.get('RETHINK_PORT')).repl()

def get_requests():
    pass

def save_request(headers, js):
    lhead = {}
    for k,v in headers:
        lhead[k] = v
    doc = {'headers': lhead, 'data': json.dumps(js)}
    r.db('relayr').table('requests').insert(doc).run()
    
