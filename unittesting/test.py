import unittest


# just for flow’s sake
# these setUp and tearDown method name is not changeable
# test can be changeable but prefix with test
class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print('setUp method execution....')

    def test(self):
        print('test method execution...')

    def tearDown(self):
        print('tearDown method execution')


# if we run as it, it will not work because be never call

# unittest.main()

