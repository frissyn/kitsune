import requests

from urllib.parse import quote

from .values import URL


def get_token(username: str, password: str) -> dict:
    data = {
        "email": quote(username),
        "password": quote(password),
        "grant_type": "password"
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    r = requests.post(URL("oauth"), data=data, headers=headers)

    print(r.text)

    r.raise_for_status()
    return r.json()


def refresh_token(token: str) -> dict:
    data = {"refresh_token": token, "grant_type": "refresh_token"}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    r = requests.post(URL("oauth"), data=data, headers=headers)

    r.raise_for_status()
    return r.json()
