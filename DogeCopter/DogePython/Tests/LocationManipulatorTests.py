import unittest
import LocationManipulator as LocationManipulator

class Test_LocationManipulatorTests(unittest.TestCase):

    def test_LocationManipulator_Constuctor_initialises_correct_values(self):
        v = {};
        brakeDuration = 1;
        ratio = 3;

        instance = LocationManipulator.LocationManipulator(v , ratio, brakeDuration);

        self.assertEquals(instance.v, {})
        self.assertEquals(instance.brakeDuration, 1);
        self.assertEquals(instance.ratio, 3);


if __name__ == '__main__':
    unittest.main()
