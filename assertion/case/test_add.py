import unittest
from add import addNum
class tools(unittest.TestCase):
    def test_add(self):
        addNum(1,2,2)
        addNum(1, 2, 3)
        addNum(3, 4, 7)
        addNum(4, 5, 9)


