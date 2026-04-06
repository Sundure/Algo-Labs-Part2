import unittest
from lab3 import Lab3

class TestLab3(unittest.TestCase):

    def test_provided_case(self):
        """Тест вашого прикладу: root(3) -> left(9) -> left(10)"""
        # Створюємо структуру:
        #      3 (root)
        #     /
        #    9 (left)
        #   /
        #  10 (right за вашим описом, хоча логічно це ліва гілка 9-ки)
        root = Lab3.BinaryTree(3)
        node_9 = Lab3.BinaryTree(9, parent=root)
        node_10 = Lab3.BinaryTree(10, parent=node_9)
        
        root.left = node_9
        node_9.left = node_10
        
        # Очікуємо 9, бо це найменше число в дереві, що більше за 3
        result = Lab3.find_successor( root)
        self.assertEqual(result, 9)

    def test_standard_bst_successor(self):
        """Тест звичайного дерева пошуку"""
        #        10
        #       /  \
        #      5    15
        #       \
        #        7
        root = Lab3.BinaryTree(10)
        n5 = Lab3.BinaryTree(5, parent=root)
        n15 = Lab3.BinaryTree(15, parent=root)
        n7 = Lab3.BinaryTree(7, parent=n5)
        root.left = n5
        root.right = n15
        n5.right = n7

        # Наступник для 5 за значенням — це 7
        self.assertEqual(Lab3.find_successor( n5), 7)
        # Наступник для 7 за значенням — це 10
        self.assertEqual(Lab3.find_successor( n7), 10)

    def test_no_successor(self):
        """Тест випадку, коли більшого числа не існує"""
        root = Lab3.BinaryTree(100)
        node_50 = Lab3.BinaryTree(50, parent=root)
        root.left = node_50
        
        # Для 100 немає більшого числа в цьому дереві
        result = Lab3.find_successor( root)
        self.assertIsNone(result)

    def test_right_branch_successor(self):
        """Тест, коли наступник знаходиться глибоко в правій гілці"""
        #   5
        #    \
        #     20
        #    /
        #   15
        root = Lab3.BinaryTree(5)
        n20 = Lab3.BinaryTree(20, parent=root)
        n15 = Lab3.BinaryTree(15, parent=n20)
        root.right = n20
        n20.left = n15
        
        # Для 5 наступне найменше більше — 15
        self.assertEqual(Lab3.find_successor( root), 15)

if __name__ == '__main__':
    unittest.main()
