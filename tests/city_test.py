import unittest

from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City("Rome", True, "Italy", "Great wine")

    def test_city_has_name(self):
        self.assertEqual("Rome", self.city.name)

    def test_city_has_been_visited(self):
        self.assertEqual(True, self.city.visited)

    def test_city_has_comment(self):
        self.assertEqual("Great wine", self.city.comment)

    def test_city_has_country(self):
        self.assertEqual("Italy", self.city.country)