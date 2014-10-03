import unittest
from Mathinator import Mathinator

class Test_UnitTestExample(unittest.TestCase):

    def test_CreateUnitVector(self):

        thing = Mathinator()

        unitx,unity,sleep = Mathinator.createUnitVector(thing,3,4,5)

        self.assertEquals(unitx, float(3)/5);
        self.assertEquals(unity, float(4)/5);
        self.assertEquals(sleep, 1)

    def test_CreateUnitVector_doesnt_blow_up_with_zero_x(self):

        thing = Mathinator()

        unitx,unity,sleep = Mathinator.createUnitVector(thing,0,4,4)

        self.assertEquals(unitx, 0);
        self.assertEquals(unity, 1);
        self.assertEquals(sleep, 1)

    def test_CreateUnitVector_doesnt_blow_up_with_zero_y(self):

        thing = Mathinator()

        unitx,unity,sleep = Mathinator.createUnitVector(thing,3,0,3)

        self.assertEquals(unitx, 1);
        self.assertEquals(unity, 0);
        self.assertEquals(sleep, 1)

if __name__ == '__main__':
    unittest.main()



