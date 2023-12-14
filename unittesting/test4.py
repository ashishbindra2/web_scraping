import unittest


#  if 2 test method are there 2 times setup method will execute 2 times tearDown method will execute
# before every test method setUp() method will be executed
# and after every test method tearDown() method will be exited
class TestCaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass method execution...")

    def setUp(self):
        print('setUp method execution....')

    def test_method1(self):
        print('test method1 execution...')

    def test_method2(self):
        print('test method2 execution...')

    def tearDown(self):
        print('tearDown method execution')

    @classmethod
    def tearDownClass(cls):
        print("teadownClass method execution")


unittest.main()
