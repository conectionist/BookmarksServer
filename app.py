from flask import Flask
from flask import request
import time
from RequestParser import RequestParser
from RequestHandler import RequestHandler
import urllib

app = Flask(__name__)
parser = RequestParser()
requestHandler = RequestHandler()

#wsgi_app = app.wsgi_app

@app.route('/')
def index():
    return time.strftime("%c")

@app.route('/bookmarks')
def bookmarks():
    link = request.args.get('link')
    tags = request.args.get('tags')
    user = request.args.get('user')

    tags = urllib.unquote(tags)

    if user is None:
        user = 'dan'

    if link is None:
        return "We were promised links"
    elif tags is None:
        return "Y u no give tags?"
    else:
        try:
            requestHandler.HandleBookmarkRequest(link, tags, user)
            return '{} with the corresponding tags ({}) have been saved to the database'.format(link, tags)
        except BaseException as ex:
            print ex
            return "There was an error. The hamsters have gone mad.";


@app.route('/bookmarks/login', methods=['POST'])
def bookmarks_login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username is None:
        return "Username is null"
    elif password is None:
        return "Password is empty"
    else:
        try:
            print "User login: " + username + " Pass: " + password
            requestHandler.handle_login_request(username, password)
            return "Welcome " + username
        except BaseException as ex:
            print ex
            return ex.message;

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
