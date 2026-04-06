import unittest
from lab2 import Lab2
from lab2 import Hamster

class TestHamsterMaxValue(unittest.TestCase):
    def test(self):
        test_cases = [
            {
                "hamsters": [Hamster(1,2), Hamster(2,2),Hamster(3,1)],
                "food": 10,
                "excepted": 3
            },
            {
                "hamsters": [Hamster(5,0), Hamster(2,2),Hamster(1,4), Hamster(5,1)],
                "food": 19,
                "excepted": 4
            },
            {
                "hamsters": [Hamster(5,0), Hamster(2,2),Hamster(1,4),],
                "food": 1,
                "excepted": 1
            },

        ]

        for case in test_cases:
            actual_result = Lab2.calculate_hamsters(case["hamsters"], case["food"])
            self.assertEqual(actual_result, case["excepted"])

if __name__ == '__main__':
    unittest.main()
