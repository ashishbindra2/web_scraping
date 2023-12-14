import pytest


@pytest.yield_fixture()
def setup_teardown():  # method name need not be setUp
    print('setUp activity')
    yield
    print('teatDown activity')


def test_method_a(setup_teardown):
    print('test_methodA execution..')


def test_method_b(setup_teardown):
    print('test_methodB execution..')
