import pytest

x_list = [1, 2, 3]
x_dict = {'key_1': 10, 'key_2': 20, 'key_3': 30}
x_value = None


# content of mazkanata.py
class TestClass(object):

    @pytest.fixture(scope="session")
    def number(self):
        assert x_value is not None, "Wrong input"
        return x_value

    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        assert x_list[0] == 1, "Wrong number!"

    def test_three(self, number):
        assert number == 5
