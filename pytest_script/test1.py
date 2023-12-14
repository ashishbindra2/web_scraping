import pytest


@pytest.fixture()
def setUp():  # method name need not be setUp
    print('setUp method')


def test_method_a(setUp):
    print('test_methodA execution..')


def test_method_b(setUp):
    print('test_methodB execution..')
