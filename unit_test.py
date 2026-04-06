import unittest
from lab1 import Lab1

# Unittest
class TestZigZagSort(unittest.TestCase):
    def test_required_matrices(self):
        test_cases = [
            {
                "name": "m=5, n=5",
                "matrix": [
                    [1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15],
                    [16, 17, 18, 19, 20],
                    [21, 22, 23, 24, 25]
                ],
                "expected": [1, 2, 6, 11, 7, 3, 4, 8, 12, 16, 21, 17, 13, 9, 5, 10, 14, 18, 22, 23, 19, 15, 20, 24, 25]
            },
            {
                "name": "m=2, n=4",
                "matrix": [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8]
                ],
                "expected": [1, 2, 5, 6, 3, 4, 7, 8]
            },
            {
                "name": "m=6, n=1",
                "matrix": [
                    [1], 
                    [2], 
                    [3], 
                    [4], 
                    [5], 
                    [6]
                ],
                "expected": [1, 2, 3, 4, 5, 6]
            },
            {
                "name": "m=1, n=1",
                "matrix": [
                [1]
            ],
                "expected": [1]
            }
        ]

        for case in test_cases:
            with self.subTest(msg=case["name"]):
                actual_result = Lab1.zig_zag_sort(case["matrix"])
                self.assertEqual(actual_result, case["expected"])

if __name__ == '__main__':
    unittest.main()

