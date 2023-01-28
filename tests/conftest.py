import pytest

class User:
    def __init__(self, name = None, second_name = None):
        self.name = name
        self.second_name = second_name

    def create(self):
        self.name = 'Pavlo'
        self.second_name = 'Znak'

        def remove(self):
        self.name = ''
        self.second_name = ''

@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()