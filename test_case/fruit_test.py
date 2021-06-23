import pytest


class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


@pytest.fixture
def my_fruit():
    yield Fruit("apple")
    raise Exception


def test_my_fruit_in_basket(my_fruit,):
    assert my_fruit is not None
