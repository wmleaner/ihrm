import unittest
suite=unittest.TestLoader().discover('.','test_case*.py')
unittest.TextTestRunner().run(suite)