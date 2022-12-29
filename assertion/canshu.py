from parameterized  import parameterized
from add import add
from ddt import ddt,data,unpack
import json

def build_add_data():
    with open('add.json')as f:
        data=json.load(f)
        print(data)
        return data
import unittest
@ddt
class Testadd(unittest.TestCase):
    @data(*build_add_data())
    @unpack
    def test_add(self,user,password):
        print(user)
        print(password)

