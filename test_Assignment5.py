import unittest
from Assignment5 import covertingTemps, fibonacciNumber


#testing out covertingTemps amd fibonacciNumber
class Assignment5Test(unittest.TestCase):

    def test_convertingTemps(self):
        self.assertAlmostEqual(covertingTemps(32), 0.0)


    def test_fibonacciNumber(self):
        self.assertAlmostEqual(fibonacciNumber(8), 21)
    


unittest.main()
