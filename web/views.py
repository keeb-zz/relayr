from flask import render_template
from flask import jsonify
from flask import request

from adapters.rethink import get_requests
from adapters.rethink import save_request

def index():
    requests = get_requests()
    return render_template('index.html', requests=requests)


def sav():
    print dir(request)
    data = request.json
    print data
    if request.json:
        print 'is a json request'
        save_request(request.headers, request.json)
        print 'returning successfully'
    else:
        print 'received unsupported request (no json data)'

    return jsonify(success="success")

    
