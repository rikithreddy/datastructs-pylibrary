from datastructs.stacks.ListStack import ListStack
import unittest

class TestArray(unittest.TestCase):


    def test_list_stack(self):
        stack = ListStack(int)

        self.assertTrue(stack.stack_empty())
        self.assertRaises(IndexError, stack.pop)
        self.assertRaises(IndexError, stack.top_elem)

        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertRaises(ValueError, stack.push, "4")

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.top_elem(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

        self.assertTrue(stack.stack_empty())



if __name__ == '__main__':
    unittest.main()
