import  unittest
from duassert import TestAssert
suit=unittest.TestSuite()
suit.addTest(TestAssert('test_eql'))
suit.addTest(TestAssert('test_eql2'))
suit.addTest(TestAssert('test_in'))
unittest.TextTestRunner().run(suit)