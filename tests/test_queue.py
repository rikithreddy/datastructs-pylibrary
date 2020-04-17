from datastructs.queues.ListQueue import ListQueue
import unittest

class TestArray(unittest.TestCase):


    def test_list_queue(self):
        queue = ListQueue(int)

        self.assertTrue(queue.queue_empty())
        self.assertRaises(IndexError, queue.dequeue)
        self.assertRaises(IndexError, queue.next_key)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertRaises(ValueError, queue.enqueue, "4")

        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.next_key(), 2)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)

        self.assertTrue(queue.queue_empty())



if __name__ == '__main__':
    unittest.main()
