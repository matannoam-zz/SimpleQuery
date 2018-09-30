from unittest import TestCase
from operator import eq, gt
from dataclasses import dataclass

from simple_query.query import Query, Matcher


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
        filtered = Query(people).filter('last_name', eq, 'Fowler')
        self.assertEqual(filtered.all(), people)

    def test_with_no_matching_items(self):
        people = [Person(last_name='Hopper')]
        filtered = Query(people).filter('last_name', eq, 'Fowler')
        self.assertEqual(filtered.all(), [])

    def test_with_only_matching_items(self):
        people = [
            Person(last_name='Fowler'), Person(last_name='Fowler'),
            Person(last_name='Fowler')]
        filtered = Query(people).filter('last_name', eq, 'Fowler')
        self.assertEqual(filtered.all(), people)

    def test_with_only_one_matching_item(self):
        people = [
            Person(last_name='Hopper'), Person(last_name='Fowler'),
            Person(last_name='Lovelace')]
        filtered = Query(people).filter('last_name', eq, 'Fowler')
        self.assertEqual(filtered.all(), people[1:2])

    def test_with_different_operator(self):
        people = [Person(last_name='Hopper')]
        filtered = Query(people).filter('last_name', gt, 'Fowler')
        self.assertEqual(filtered.all(), people)


class MatcherTests(TestCase):

    def test_does_not_match(self):
        matcher = Matcher(eq, 'Fowler')
        self.assertFalse(matcher.matches('Hopper'))

    def test_does_match(self):
        matcher = Matcher(eq, 'Fowler')
        self.assertTrue(matcher.matches('Fowler'))

    def test_other_operator(self):
        matcher = Matcher(gt, 'Fowler')
        self.assertTrue(matcher.matches('Hopper'))
