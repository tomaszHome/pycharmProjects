import pytest

x_list = [1, 2, 3]
x_dict = {'key_1': 10, 'key_2': 20, 'key_3': 30}
x_value = 2
# number = 5


# content of mazkanata.py
class TestClass(object):

    @pytest.fixture(scope="class")
    def number(self):
        assert x_value is not None, "Wrong input"
        return x_value


    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        assert x_list[0] == 1, "Wrong number!"



    @pytest.mark.usefixtures("number")
    def test_three(self, request):
        def print_info():
            print "teardown"
        request.addfinalizer(lambda: print_info)
        assert number == 5
