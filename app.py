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

    price = {'モントレー':1000, 'ぺパロニサラミ':1500, 'テリヤキチキン':2000, 'ナスミート':2500}

    speech = type + "、" + size + "サイズ、" + sauce + "ソース、" + crust + "でご注文承りました。料金は" + price + "円です。30分少々でお届けに上がります！"

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
