#断言封装


def assertionuse(self,resp,is_success,code,message):
    self.assertEqual(is_success,resp.json().get('success'))
    self.assertEqual(code,resp.json().get('code'))
    self.assertEqual(message,resp.json().get('message'))


