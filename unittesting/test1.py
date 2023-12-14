import unittest


# just for flow’s sake
# these setUp and tearDown method name is not changeable
# test can be changeable but prefix with test
class TestCase2(unittest.TestCase):
    def setUp(self):
        print('from test 1 setUp method execution....')

    def test(self):
        print('test test 1 method execution...')

    def tearDown(self):
        print('tearDown test 1 method execution')


# if we run as it, it will not work because be never call

# unittest.main()

