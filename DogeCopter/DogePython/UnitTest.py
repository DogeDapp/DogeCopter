import unittest

class Test_UnitTestExample(unittest.TestCase):
    def test_Addition_return_sum_of_two_numbers(self):
        result = 1 + 1
        self.assertEquals(2, result)

if __name__ == '__main__':
    unittest.main()



