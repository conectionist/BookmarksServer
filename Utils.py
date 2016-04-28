import datetime
import time


def get_default_cookie_expiration_date():
    expires = time.time() + 60 * 10  # 10 minutes
    return time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime(expires))
