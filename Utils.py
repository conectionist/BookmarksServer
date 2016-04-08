import datetime
import time


def get_default_cookie_expiration_date():
    expires = time.time() + 60  # 1 minute
    return time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime(expires))
