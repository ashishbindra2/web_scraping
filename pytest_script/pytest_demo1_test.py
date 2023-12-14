import pytest


def test_method_a():
    print('test_methodA execution')


def test_method_b():
    print('test_methodB execution')


# pytest not go consider because it is not pytest understandable form
def my_own_test_method():
    print('my_owntest_method execution')
