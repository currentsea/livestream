import json
import datetime
import requests
from flask import Flask

from flask import request
from flask import jsonify
from flask import redirect
from flask import render_template


app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def hello_world():
    #the_date_variable
    the_date_today = datetime.datetime.utcnow()
    the_date_string = the_date_today.strftime('%Y-%m-%d %H:%M:%S %Z')
    return render_template('index.html', the_date_variable=the_date_string)

@app.route('/hello/<name>')
def hello_name(name):
    print (request.args)
    return 'Hello ' + name

@app.route('/api/1.0/<symbol>/price')
def get_btc_price(symbol):
    req_url = 'https://www.okcoin.com/api/v1/ticker.do?symbol=' + symbol
    req = requests.get(req_url)
    if req.status_code >= 400:
        raise IOError("The response code was above 400. Something went wrong. " + str(req.status_code))
    else:
        print ("The request was successful - response code: " + str(req.status_code))
    response_data = req.json()
    return jsonify(response_data)


@app.route('/hello/')
def hello_no_params():
    return redirect('/')

if __name__ == '__main__':
    app.run()
