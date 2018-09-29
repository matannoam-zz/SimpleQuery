from unittest import TestCase

from simple_query.query import Query


class QueryAllTests(TestCase):

    def test_with_no_items(self):
        items = []
        query = Query(items)
        self.assertEqual(query.all(), items)
