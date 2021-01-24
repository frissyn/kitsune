def URL(endpoint: str) -> str: return BASE_URL + ENDPOINTS[endpoint]

BASE_URL = "https://" + "kitsu.io/api/"

HEADERS = {
    "Authorization": None,
    "Accept": "application/vnd.api+json",
    "Content-Type": "application/vnd.api+json",
}

ENDPOINTS = {
    "anime_collection": "edge/anime",
    "anime_resource": "edge/anime/{id}",

    "anime_character_collection": "edge/anime-characters",
    "anime_character_resource": "edge/anime-characters/{id}",

    "episode_collection": "edge/episodes",
    "episode_resource": "edge/episodes/{id}",

    "categories_collection": "edge/categories",
    "categories_resource": "edge/categories/{id}",

    "chapter_collection": "edge/chapters",
    "chapter_resource": "edge/chapters/{id}",

    "characters_collection": "edge/characters",
    "characters_resource": "edge/characters/{id}",

    "oauth": "oauth/token",

    "trending_anime_collection": "edge/trending/anime",
    "trending_manga_collection": "edge/trending/manga",

    "manga_collection": "edge/manga",
    "manga_resource": "edge/manga/{id}",

    "manga_character_collection": "edge/manga-characters",
    "manga_character_resource": "edge/manga-characters/{id}"
}
