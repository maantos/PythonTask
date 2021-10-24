from PythonTasks.Pythonds.fractionClass import Fraction
import unittest

class TestFraction(unittest.TestCase):
    def testAddFraction(self):
        f1 = Fraction(1,2)+Fraction(2,4)
        self.assertEqual(f1.num , 1, "Num Pass")
        self.assertEqual(f1.den , 1, "Num Pass")

    def testPrinting(self):
        f1 = Fraction(4,5)
        self.assertEqual(f1.__str__(), '4/5')

        #Tested class...




if __name__ == '__main__':
    unittest.main()