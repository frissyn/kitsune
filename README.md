# kitsune

**This project is a work in progress, currently in a pre-alpha release.**

Kitsune is a simple and extensible Python API wrapper for the Kitsu Anime/Manga API. I only intend to cover the following endpoints:
- Anime
- Manga
- Categories
- Characters

Kitsune will be for getting information directly related manga and anime. The "social media" (so to speak) portion of Kistu will be ignored as much as possible, only being referenced when absoultely necessary. Objects that link to Kistu users, posts, etc. will be ommited.

# Overview

### Installation

|Manager          |Command                           |
|:----------------|:---------------------------------|
|**pip**          |`pip install kitsune.py`          |
|**poetry**       |`python -m poetry add kitsune.py` |
|**easy_install** |`easy_install kitsune.py`         |

### Usage

**Again, this is a work in progress, consider these implementation notes.**

Without authentication:
```python
from kitsune import Client

client = Client.new()

anime = client.search_anime("Coboy Bebop")
manga = client.search_manga("Rent A Girlfriend")
```

Using user authentication:
```python
from kitsune import Client

client = Client.authenticate(username="user123", password="wordpass")

collection = client.get_category("Comedy")
```

### Testing and Contributing

1. Clone the repository with `git`:

   - `git clone https://github.com/frissyn/kitsune.git`
   - `cd kitsune`

2. Make your changes
3. Run tests from with the bin script:

   - `bash bin/test.sh`
   - Make sure all tests pass!

