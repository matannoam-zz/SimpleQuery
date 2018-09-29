from unittest import TestCase
from operator import eq
from dataclasses import dataclass

from simple_query.query import Query


class QueryAllTests(TestCase):

    def test_with_no_items(self):
        items = []
        query = Query(items)
        self.assertEqual(query.all(), items)

    def test_with_some_items(self):
        items = ['One', 'Two', 'Three']
        query = Query(items)
        self.assertEqual(query.all(), items)


@dataclass
class Person:
    last_name: str


class QueryFilterTests(TestCase):

    def test_with_no_items(self):
        people = []
        query = Query(people)
        self.assertEqual(query.filter('last_name', eq, 'Fowler'), people)

    def test_with_no_matching_items(self):
        people = [Person(last_name='Hopper')]
        query = Query(people)
        self.assertEqual(query.filter('last_name', eq, 'Fowler'), [])
