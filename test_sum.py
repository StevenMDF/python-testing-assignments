import unittest
from task1 import sum

class TESTSUM(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(2,3),5, "2 plus 3 should be 5")

if __name__=='__main__':
    unittest.main()
