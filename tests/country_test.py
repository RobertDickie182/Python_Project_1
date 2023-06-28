import unittest

from models.country import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country("England")

    def test_country_has_name(self):
        self.assertEqual("England", self.country.name)