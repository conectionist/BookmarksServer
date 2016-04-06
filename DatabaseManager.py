from Database import Database
import MySQLdb
from Logger import Logger

log = Logger().logger


class DatabaseManager:
    def __init__(self):
        self.db = Database()

    def save_entry(self, table, column, entry, column2 = None, entry2 = None):
        entries = (entry,)

        if column2 is None:
            query = """
                insert into {}({})
                values(%s)
                """.format(table, column)

        else:
            query = """
                insert into {}({},{})
                values(%s, %s)
                """.format(table, column, column2)

            entries = (entry, entry2)

        try:
            self.db.insert(query, entries)

        except MySQLdb.Error as ex:
            if ex.args[0] == 1062:
                print ex.args[1]
            else:
                log.debug("Failed to perform db insert operation. Ex:")
                log.debug(ex.message)

    def get_id_of_value(self, table, column, value):
        select_query = """
                   SELECT id
                   FROM {}
                   WHERE {} = %s
                   """.format(table, column)

        ids_list = self.db.query(select_query, (value,))

        return ids_list[0]['id']

    def create_association_entry(self, assoc_table, table1, table2, column1, column2, value1, value2):
        id1 = self.get_id_of_value(table1, column1, value1)
        id2 = self.get_id_of_value(table2, column2, value2)

        # insert operation
        query = """
                insert into {}
                values(%s,%s)
                """.format(assoc_table)

        try:
            print "Running query: \n" + query
            self.db.insert(query, (id1, id2))

        except MySQLdb.Error as ex:
            if ex.args[0] == 1062:
                log.debug(ex.args[1])
            else:
                log.debug("Failed to perform db insert operation. Ex:")
                log.debug(ex.message)

    def save_link(self, link, title):
        self.save_entry('links', 'link', link, 'title', title)

    def save_user(self, user):
        self.save_entry('users', 'nume', user)

    def save_tag(self, tag):
        self.save_entry('tags', 'nume', tag)

    def create_user_link(self, user, link):
        self.create_association_entry('UserLinks', 'links', 'users', 'link', 'nume', link, user)

    def create_link_tag_association(self, link, tag):
        self.create_association_entry('LinksTagAssociation', 'links', 'tags', 'link', 'nume', link, tag)

    def get_password_for_user(self, username):
        select_query = """
            SELECT parola
            FROM users
            WHERE nume = %s
            """

        log.debug("login query:")
        log.debug(select_query)

        return self.db.query(select_query, (username,))
