BASE_URL = "https://" + "kitsu.io/api/"

HEADERS = {
    "Authorization": None,
    "Accept": "application/vnd.api+json",
    "Content-Type": "application/vnd.api+json",
}

ENDPOINTS = {
    "ouath": "oauth/token"
}

def url(endpoint: str):
    return BASE_URL + ENDPOINTS[endpoint]
