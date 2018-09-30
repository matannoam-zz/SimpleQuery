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


class Matcher:

    def __init__(self, operator, value):
        self.value = value
        self.operator = operator

    def matches(self, target_value):
        return self.operator(target_value, self.value)
