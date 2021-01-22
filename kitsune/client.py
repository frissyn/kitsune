import requests

from .auth import get_token

from .values import HEADERS


req = requests.Session()
req.headers.update(HEADERS)


class Client(object):
    def __init__(self, session: requests.Session, token: dict):
        self.token = token
        self.session = session
        
        try:
            self.auth_string = token["access_token"]
        except KeyError:
            self.auth_string = None

    @classmethod
    def new(cls):
        return cls(req)

    @classmethod
    def authenticate(cls, username: str, password: str):
        token = get_token(username, password)

        req.headers.update({
            "Authorization": f"Bearer {token['access_token']}"
        })

        return cls(req, token)
