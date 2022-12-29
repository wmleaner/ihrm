import unittest
class TestAssert(unittest.TestCase):
    def test_eql(self):
        self.assertEqual(10,10)
    def test_eql2(self):
        self.assertEqual(10,100)
    def test_in(self):
        self.assertIn('aaa','aaa112seqaswzdcxs')

