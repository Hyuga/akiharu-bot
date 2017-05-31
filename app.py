#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "order":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    type = parameters.get("type")
    size = parameters.get("size")
    sauce = parameters.get("sauce")
    crust = parameters.get("crust")

    price = {'�����g���[':1000, '�؃p���j�T���~':1500, '�e�����L�`�L��':2000, '�i�X�~�[�g':2500}

    speech = type + "�A" + size + "�T�C�Y�A" + sauce + "�\�[�X�A" + crust + "�ł���������܂����B������" + price + "�~�ł��B30�����X�ł��͂��ɏオ��܂��I"

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "agent"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
