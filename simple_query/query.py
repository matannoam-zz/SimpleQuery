class Query:

    def __init__(self, data):
        self.data = [item for item in data]

    def all(self):
        return self.data

    def filter(self, field, operator, value):

        def matches_value(target):
            return operator(target, value)

        def get_field(item):
            return getattr(item, field)

        def field_matches_value(item):
            return matches_value(get_field(item))

        return Query(
            item for item in self.data
            if field_matches_value(item))


class Filter:

    def __init__(self, field, operator, value):
        pass

    def matches_value(self, target_value):
        return False
