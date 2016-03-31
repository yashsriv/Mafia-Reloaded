"""
Server for mafia
"""
from flask import Flask, request, render_template, abort
APP = Flask(__name__)
CLIENTS = []
GAME_STARTED = False

@APP.route('/')
def index():
    """
    Index page
    """
    return render_template('index.html')

@APP.route('/poll')
def poll():
    """
    Send constant data to a poller
    """
    return "This is a reply"

@APP.route('/status')
def status():
    """
    Status Page
    """
    message = 'Welcome To Mafia Reloaded\n'
    message = 'MAX_NUM = ' + str(MAX_NUM) + '\n'
    message += 'CLIENTS = ' + str(CLIENTS) + '\n'
    message += 'GAME_STARTED = ' + str(GAME_STARTED) + '\n'
    return message

@APP.route('/main/', methods=['GET', 'POST'])
@APP.route('/main/<username>', methods=['GET'])
def add_user(username=None):
    """
    Adds client to current users

    Using either POST request to main
    or GET request to main/username
    """
    if request.method == 'POST':
        username = request.form['user']
    if username not in CLIENTS and len(CLIENTS) < MAX_NUM:
        CLIENTS.append(username)
    if len(CLIENTS) == MAX_NUM:
        global GAME_STARTED
        GAME_STARTED = True
    if username in CLIENTS and GAME_STARTED:
        return ('###').join(CLIENTS)
    else:
        abort(501)


if __name__ == '__main__':
    global MAX_NUM
    MAX_NUM = int(input('Enter required number of clients:'))
    APP.run(host='0.0.0.0', debug=True)
