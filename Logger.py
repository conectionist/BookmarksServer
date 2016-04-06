import logging


class Logger:
    def __init__(self):
        self.logger = logging.getLogger('myapp')
        hdlr = logging.FileHandler('bookmarks_server.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        self.logger.addHandler(hdlr)
        self.logger.setLevel(logging.DEBUG)
