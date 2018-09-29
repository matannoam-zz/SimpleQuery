class Query:

    def __init__(self, data):
        self.data = data

    def all(self):
        return [item for item in self.data]
