import unittest
from datastructs.queues.ListQueue import ListQueue
from datastructs.exceptions.custom import (
                            InvalidDataType,
                            QueueEmpty
                            )

class TestQueue(unittest.TestCase):


    def test_list_queue(self):
        queue = ListQueue(int)

        self.assertTrue(queue.queue_empty())
        self.assertRaises(QueueEmpty, queue.dequeue)
        self.assertRaises(QueueEmpty, queue.next_key)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertRaises(InvalidDataType, queue.enqueue, "4")

        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.next_key(), 2)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)

        self.assertTrue(queue.queue_empty())



if __name__ == '__main__':
    unittest.main()
