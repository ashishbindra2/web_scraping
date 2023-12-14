import pytest


@pytest.yield_fixture(scope='module')
def setup_teardown_class():  # method name need not be setUp
    print('setUpClass activity')
    yield
    print('teatDownClass activity')


def test_method_a(setup_teardown_class):
    print('test_methodA execution..')


def test_method_b(setup_teardown_class):
    print('test_methodB execution..')
