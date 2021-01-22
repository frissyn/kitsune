import requests

from .values import HEADERS
from .values import BASE_URL


req = requests.Session()
req.headers.update(HEADERS)


class Client(object):
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def new(cls, *args, **kwargs):
        pass    

    @classmethod
    def authenticate(cls, username=None, password=None):
        pass
