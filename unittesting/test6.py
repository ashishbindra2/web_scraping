# implementation of test suit
import unittest

from test import *
from test1 import *

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo)  # from test case can you load all test
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)

ts = unittest.TestSuite([tc1, tc2])  # create test suit
unittest.TextTestRunner().run(ts)  # run test suit
