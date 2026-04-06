import unittest
from lab4 import PriorityQueue

class TestRedBlackPriorityQueue(unittest.TestCase):
    def setUp(self):
        """Ініціалізація нової черги перед кожним тестом."""
        self.pq = PriorityQueue()

    def test_insert_and_peek(self):
        """Перевірка вставки та отримання елемента з найвищим пріоритетом без видалення."""
        self.pq.insert("low_task", 1)
        self.assertEqual(self.pq.peek().value, "low_task")
        
        self.pq.insert("high_task", 10)
        self.assertEqual(self.pq.peek().value, "high_task")
        
        self.pq.insert("medium_task", 5)
        self.assertEqual(self.pq.peek().value, "high_task")

    def test_pop_order(self):
        """Перевірка правильного порядку видалення елементів (від найбільшого пріоритету до найменшого)."""
        self.pq.insert("task_p3", 3)
        self.pq.insert("task_p10", 10)
        self.pq.insert("task_p1", 1)
        self.pq.insert("task_p7", 7)

        # Очікуємо, що першим вийде елемент з пріоритетом 10
        popped_1 = self.pq.pop()
        self.assertIsNotNone(popped_1)
        self.assertEqual(popped_1.value, "task_p10") 
        
        # Далі пріоритет 7
        popped_2 = self.pq.pop()
        self.assertIsNotNone(popped_2)
        self.assertEqual(popped_2.value, "task_p7")

        # Далі пріоритет 3
        popped_3 = self.pq.pop()
        self.assertIsNotNone(popped_3)
        self.assertEqual(popped_3.value, "task_p3")

    def test_empty_queue(self):
        """Перевірка поведінки порожньої черги."""
        self.assertIsNone(self.pq.peek())
        self.assertIsNone(self.pq.pop())

if __name__ == '__main__':
    unittest.main()
