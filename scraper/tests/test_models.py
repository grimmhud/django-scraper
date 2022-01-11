from django.test import TestCase
from ..models import ScrapingResult, ScrapingSearch


class ScrapingResultTestCase(TestCase):
    def setUp(self):
        self.array = ['row-1', 'row-2', 'row-3']

    def test_set_created_at_automatic(self):
        result = ScrapingResult.create(self.array)

        self.assertTrue(result.created_at != None)

    def test_all_values_is_set_correctly(self):
        result = ScrapingResult.create(self.array)

        self.assertListEqual(self.array, result.values)


class ScrapingSearchTestCase(TestCase):
    def test_set_created_at_automatic(self):
        search = ScrapingSearch.create('self.array', 'self.array', ScrapingResult.create(['row-1']))

        self.assertTrue(search.created_at != None)