import json
import uuid

class User:
    def __init__(self, nume, oras):
        self.id = str(uuid.uuid4())
        self.nume = nume
        self.oras = oras
        self.rating = 0

    def getId(self):
        return self.id