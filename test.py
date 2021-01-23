import unittest
import requests

from kitsune import Client

from kitsune.params import with_fields
from kitsune.params import with_filter
from kitsune.params import with_sorting
from kitsune.params import with_includes


class TestClient(unittest.TestCase):
    def test_client_session(self):
        res = Client.new().session
        test = requests.Session

        self.assertIsInstance(res, test)

    def test_client_token(self):
        res = Client.new().auth_string
        test = None

        self.assertEqual(res, test)


class TestUtilities(unittest.TestCase):
    def test_with_filter(self):
        res = with_filter(categories="adventure")
        test = {"filter[categories]": "adventure"}

        self.assertEqual(res, test)

    def test_with_fields(self):
        res = with_fields("users", ["name", "createdAt"])
        test = {"fields[users]": "name,createdAt"}

        self.assertEqual(res, test)

    def test_with_includes(self):
        res = with_includes(["categories", "mediaRelationships.destination"])
        test = {"includes": "categories,mediaRelationships.destination"}

        self.assertEqual(res, test)

    def test_with_sorting(self):
        res = with_sorting(["followersCount", "followingCount"])
        test = {"sort": "-followersCount,-followingCount"}

        self.assertEqual(res, test)


if __name__ == "__main__":
    unittest.main()
