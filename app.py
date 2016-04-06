from flask import Flask
from flask import request
import time
from RequestParser import RequestParser
from RequestHandler import RequestHandler
import urllib
from Logger import Logger

app = Flask(__name__)
parser = RequestParser()
requestHandler = RequestHandler()
log = Logger().logger


@app.route('/')
def index():
    return time.strftime("%c")


@app.route('/bookmarks')
def bookmarks():
    log.debug('received new bookmark request:')
    log.debug(request)
    link = request.args.get('link')
    title = request.args.get('title')
    tags = request.args.get('tags')
    user = request.args.get('user')

    tags = urllib.unquote(tags)

    if user is None:
        user = 'dan'

    if link is None:
        return "We were promised links"
    elif title is None:
        return "No page title?"
    elif tags is None:
        return "Y u no give tags?"
    else:
        try:
            requestHandler.handle_bookmark_request(link, title, tags, user)
            return '{} with the corresponding tags ({}) have been saved to the database'.format(link, tags)
        except BaseException as ex:
            log.debug(ex.message)
            return "There was an error. The hamsters have gone mad.";


@app.route('/bookmarks/login', methods=['POST'])
def bookmarks_login():
    log.debug('received new login request:')
    log.debug(request)

    username = request.form.get('username')
    password = request.form.get('password')

    if username is None:
        return "Username is null"
    elif password is None:
        return "Password is empty"
    else:
        try:
            log.debug("User login: " + username + " Pass: " + password)
            requestHandler.handle_login_request(username, password)
            return "Welcome " + username
        except BaseException as ex:
            log.debug(ex.message)
            return ex.message;

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
