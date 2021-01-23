import json
import requests

from .values import url


def get_token(username: str, password: str) -> dict:
    data = {
        "username": username,
        "password": password,
        "grant_type": "password"
    }

    headers = {"Content-Type": "application/json"}
    r = requests.post(url("oauth"), json=json.dumps(data), headers=headers)

    r.raise_for_status()
    return r.json()


def refresh_token(token: str) -> dict:
    data = {
        "refresh_token": token,
        "grant_type": "refresh_token"
    }

    headers = {"Content-Type": "application/json"}
    r = requests.post(url("oauth"), json=json.dumps(data), headers=headers)

    r.raise_for_status()
    return r.json()
