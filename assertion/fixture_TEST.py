import  unittest
class Testlogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('打开浏览器')
    def setUp(self) -> None:
        print('打开网页，点击登录')
    def test_1(self):
        print('case1')
    def test_2(self):
        print('case2')
    def test_3(self):
         print('case3')
    def tearDown(self) -> None:
        print('关闭网页')
    @classmethod
    def tearDownClass(cls) -> None:
        print('关闭浏览器')
