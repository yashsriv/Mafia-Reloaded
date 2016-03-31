"""
Server for mafia
"""
from flask import Flask, request
APP = Flask(__name__)
CLIENTS = []
GAME_STARTED = False

@APP.route('/status')
def status():
    """
    Status Page
    """
    message = 'Welcome To Mafia Reloaded\n'
    if GAME_STARTED:
        message += 'Game Has Been Started\n'
        message += 'Connected Players :\n'
        message += ('\n').join(CLIENTS)
    return message

@APP.route('/main/', methods=['GET', 'POST'])
def add_user():
    """
    Adds client to current users
    """
    if request.method == 'POST':
        if request.form['user'] not in CLIENTS and len(CLIENTS) < MAX_NUM:
            CLIENTS.append(request.form['user'])
            if len(CLIENTS) == MAX_NUM:
                global GAME_STARTED
                GAME_STARTED = True

if __name__ == '__main__':
    global MAX_NUM
    MAX_NUM = int(input('Enter required number of clients:'))
    APP.run(host='0.0.0.0', debug=True)
