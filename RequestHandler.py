from RequestParser import RequestParser
from DatabaseManager import DatabaseManager
from Logger import Logger

log = Logger().logger


class RequestHandler:
    def __init__(self):
        self.requestParser = RequestParser()
        self.dbmgr = DatabaseManager()

    def save_bookmark_to_database(self, link, title, tags, user):
        self.dbmgr.save_link(link, title)

        for tag in tags:
            self.dbmgr.save_tag(tag)

        self.dbmgr.create_user_link(user, link)
        self.dbmgr.create_link_tag_association(link, tag)

    def handle_bookmark_request(self, link, title, tags, user):
        tags_list = self.requestParser.getTags(tags)

        self.save_bookmark_to_database(link, title, tags_list, user)
        log.debug("Saved {} with title '{}' and tags '{}' for user '{}'".format(link, title, tags, user))

    def handle_login_request(self, username, password):
        passwords = self.dbmgr.get_password_for_user(username)
        if 0 == len(passwords):
            raise BaseException("Username not found")

        pwd = passwords[0]['parola']

        if pwd != password:
            raise BaseException("Invalid password")
