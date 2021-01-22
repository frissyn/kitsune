import requests

from .values import HEADERS
from .values import BASE_URL


req = requests.Session()
req.headers.update(HEADERS)


class Client(object):
    fetch = req

    def __init__(self, KEY):
        pass