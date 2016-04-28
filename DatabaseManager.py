from Database import Database
import MySQLdb
from Logger import Logger

log = Logger.get_instance().logger


class DatabaseManager:
    def __init__(self):
        self.db = Database()

    def call_db_procedure(self, proc_name, params):
        log.debug("Calling procedure {} with params {}".format(proc_name, params))

        try:
            self.db.call_procedure(proc_name, params)

        except MySQLdb.Error as ex:
            if ex.args[0] == 1062:
                print ex.args[1]
            else:
                log.debug("Failed to perform db insert operation. Ex:")
                log.debug(ex)

    def get_results_from_db_procedure(self, proc_name, params):
        log.debug("Calling procedure {} with params {}".format(proc_name, params))

        try:
            return self.db.call_procedure_and_return_results(proc_name, params)
        except MySQLdb.Error as ex:
            if ex.args[0] == 1062:
                print ex.args[1]
            else:
                log.debug("Failed to perform db insert operation. Ex:")
                log.debug(ex)

    def save_link(self, link, title):
        self.call_db_procedure('save_link', [link, title])

    def save_user(self, user, password):
        self.call_db_procedure('save_user', [user, password])

    def save_tag(self, tag):
        self.call_db_procedure('save_tag', [tag])

    def create_user_link(self, user, link):
        self.call_db_procedure('create_user_link', [user, link])

    def create_link_tag_association(self, link, tag):
        self.call_db_procedure('create_link_tag_association', [link, tag])

    def get_password_for_user(self, username):
        select_query = "select get_user_password(%s) as 'password'"

        log.debug("login query:")
        log.debug(select_query)

        return self.db.query(select_query, (username,))

    def get_bookmarks_for_user(self, username):
        return self.get_results_from_db_procedure('get_user_bookmarks', [username])
