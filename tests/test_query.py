from unittest import TestCase
from operator import eq, gt
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

    def test_with_only_matching_items(self):
        people = [
            Person(last_name='Fowler'), Person(last_name='Fowler'),
            Person(last_name='Fowler')]
        query = Query(people)
        self.assertEqual(query.filter('last_name', eq, 'Fowler'), people)

    def test_with_only_one_matching_item(self):
        people = [
            Person(last_name='Hopper'), Person(last_name='Fowler'),
            Person(last_name='Lovelace')]
        query = Query(people)
        self.assertEqual(query.filter('last_name', eq, 'Fowler'), people[1:2])

    def test_with_different_operator(self):
        people = [Person(last_name='Hopper')]
        query = Query(people)
        self.assertEqual(query.filter('last_name', gt, 'Fowler'), people)
