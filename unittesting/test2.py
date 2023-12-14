import unittest


# just for flow’s sake
# these setUp and tearDown method name is not changeable
# test can be changeable but prefix with test
class TestCasesDemo(unittest.TestCase):
    def setUp(self):
        print('setUp method execution....')

    def test_method(self):
        print('test method execution...')
        a = 10/0

    def tearDown(self):
        print('tearDown method execution')


# if we run as it, it will not work because be never call

unittest.main()

