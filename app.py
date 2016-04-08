from flask import Flask
from flask import request
from flask import render_template
from flask import make_response

import time
import urllib

from RequestParser import RequestParser
from RequestHandler import RequestHandler
from Logger import Logger
from Exceptions import InvalidParameterException
import Utils

app = Flask(__name__)
parser = RequestParser()
requestHandler = RequestHandler()
log = Logger.get_instance().logger


@app.route('/')
def index():
    username = request.cookies.get('username')

    if username is None:
        return "Not logged in"
    else:
        return "Hello, {}!<br><br> The time is {}".format(username, time.strftime("%c"))


@app.route('/bookmarks/login')
def login():
    return render_template('login.html')


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

    try:
        validate_bookmark_parameters(link, title, tags)

        requestHandler.handle_bookmark_request(link, title, tags, user)

        answer = '{} with the corresponding tags ({}) have been saved to the database'.format(link, tags)
        log.debug(answer)

        return answer
    except InvalidParameterException as ipx:
        log.debug(ipx.get_message())
        return ipx.get_message()
    except BaseException as ex:
        log.debug(ex.message)
        return "There was an error. The hamsters have gone mad."


@app.route('/bookmarks/auth', methods=['POST'])
def bookmarks_auth():
    log.debug('received new login request:')
    log.debug(request)

    username = request.form.get('username')
    password = request.form.get('password')

    try:
        validate_login_params(username, password)

        log.debug("User login: " + username + " Pass: " + password)
        requestHandler.handle_login_request(username, password)

        resp = make_response(render_template('welcome.html', username = username))
        log.debug("expiration date: ")
        log.debug(Utils.get_default_cookie_expiration_date())
        resp.set_cookie('username', value=username, expires=Utils.get_default_cookie_expiration_date())
        return resp

    except InvalidParameterException as ipx:
        log.debug(ipx.get_message())
        return ipx.get_message()
    except BaseException as ex:
        log.debug(ex.message)
        return ex.message


def validate_login_params(username, password):
    if username is None:
        raise InvalidParameterException("Username is null")
    elif password is None:
        raise InvalidParameterException("Password is empty")


def validate_bookmark_parameters(link, title, tags):
    if link is None:
        raise InvalidParameterException("We were promised links")
    elif title is None:
        raise InvalidParameterException("No page title?")
    elif tags is None:
        raise InvalidParameterException("Y u no give tags?")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
