from RequestParser import RequestParser
from Database import Database
import MySQLdb


class RequestHandler:
    def __init__(self):
        self.requestParser = RequestParser()
        self.db = Database()

    def save_entry(self, entry, entry_type):
        table = ""
        column = ""

        if entry_type == 'user':
            table = 'users'
            column = 'nume'
        elif entry_type == 'link':
            table = 'links'
            column = 'link'
        elif entry_type == 'tag':
            table = 'tags'
            column = 'nume'
        else:
            print "save_entry: Got invalid entry type: " + entry_type
            return

        query = """
            insert into {}({})
            values('{}')
            """.format(table, column, entry)

        try:
            self.db.insert(query)

        except MySQLdb.Error as ex:
            if ex.args[0] == 1062:
                print ex.args[1]
            else:
                print "Failed to perform db insert operation. Ex:"
                print ex

    def create_association_entry(self, entity1, entity2, table, value1, value2):
        table1 = ""
        column1 = ""
        fk1 = ""
        table2 = ""
        column2 = ""
        fk2 = ""

        if entity1 == 'user':
            table1 = "users"
            column1 = "nume"
            fk1 = "user_id"
        elif entity1 == 'link':
            table1 = "links"
            column1 = "link"
            fk1 = "link_id"
        elif entity1 == 'tag':
            table1 = "tags"
            column1 = "nume"
            fk1 = "tag_id"
        else:
            print "create_association_entry: Got invalid entity: " + entity1
            return

        if entity2 == 'user':
            table2 = "users"
            column2 = "nume"
            fk2 = "user_id"
        elif entity2 == 'link':
            table2 = "links"
            column2 = "link"
            fk2 = "link_id"
        elif entity2 == 'tag':
            table2 = "tags"
            column2 = "nume"
            fk2 = "tag_id"
        else:
            print "create_association_entry: Got invalid entity: " + entity2
            return

        # first query
        select_query1 = """
                   SELECT id
                   FROM {}
                   WHERE {} = '{}'
                   """.format(table1, column1, value1)

        ids_list1 = self.db.query(select_query1)

        id1 = ids_list1[0]['id']

        # second query
        select_query2 = """
                   SELECT id
                   FROM {}
                   WHERE {} = '{}'
                   """.format(table2, column2, value2)

        ids_list2 = self.db.query(select_query2)

        id2 = ids_list2[0]['id']

        # insert operation
        query = """
                insert into {}
                values({},{})
                """.format(table, id1, id2)

        try:
            print "Running query: \n" + query
            self.db.insert(query)

        except MySQLdb.Error as ex:
            if ex.args[0] == 1062:
                print ex.args[1]
            else:
                print "Failed to perform db insert operation. Ex:"
                print ex

    def save_link(self, link):
        self.save_entry(link, "link")

    def save_user(self, user):
        self.save_entry(user, "user")

    def save_tag(self, tag):
        self.save_entry(tag, "tag")

    def create_user_link(self, user, link):
        self.create_association_entry('link', 'user', 'UserLinks', link, user)

    def create_link_tag_association(self, link, tag):
        self.create_association_entry('link', 'tag', 'LinksTagAssociation', link, tag)

    def SaveBookmarkToDatabase(self, link, tagsList, user):
        #self.save_user(user)
        self.save_link(link)

        for tag in tagsList:
            self.save_tag(tag)

        self.create_user_link(user, link)
        self.create_link_tag_association(link, tag)

    def HandleBookmarkRequest(self, link, tags, user):
        tagsList = self.requestParser.getTags(tags)

        self.SaveBookmarkToDatabase(link, tagsList, user)
        print "Saved {} with tags '{}' for user '{}'".format(link, tags, user)

    def handle_login_request(self, username, password):
        select_query = """
            SELECT parola
            FROM users
            WHERE nume = '{}'
            """.format(username)

        passwords = self.db.query(select_query)
        if 0 == len(passwords):
            raise BaseException("Username not found")

        pwd = passwords[0]['parola']

        if pwd != password:
            raise BaseException("Invalid password");