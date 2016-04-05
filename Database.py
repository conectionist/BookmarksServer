import MySQLdb


class Database:

    host = 'localhost'
    user = 'ionica'
    password = 'parola'
    db = 'bookmarks'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insert(self, query, params):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
        except MySQLdb.Error as ex:
            self.connection.rollback()
            raise ex

    def query(self, query, params):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query, params)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()
