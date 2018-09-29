class Query:

    def __init__(self, data):
        self.data = data

    def all(self):
        return [item for item in self.data]

    def filter(self, field, operator, value):
        return [
            item for item in self.data
            if getattr(item, field) == value]
