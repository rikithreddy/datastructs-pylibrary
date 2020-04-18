import unittest
from datastructs.lists.SingleLinkList import SingleLinkList
from datastructs.exceptions.custom import (
                                    InvalidDataType,
                                    LinkedListEmpty
                                    )

class TestSingleLinkList(unittest.TestCase):

    def list_operations(self, custom_list):
        self.assertRaises(LinkedListEmpty, custom_list.pop_first_element)
        self.assertRaises(LinkedListEmpty, custom_list.get_first_element)
        self.assertRaises(LinkedListEmpty, custom_list.get_last_element)
        self.assertTrue(custom_list.list_empty())
        custom_list.add_to_front(0)
        custom_list.add_to_back(1)
        self.assertEqual(custom_list.get_last_element(), 1)
        self.assertEqual(custom_list.get_first_element(), 0)
        custom_list.add_to_back(2)
        custom_list.add_to_front(3)
        self.assertEqual(custom_list.pop_first_element(), 3)
        self.assertEqual(custom_list.pop_first_element(), 0)
        self.assertFalse(custom_list.list_empty())

        __, index = custom_list.find_element(2).__next__()
        self.assertEqual(index, 1)
        self.assertFalse(custom_list.has_element(0))
        self.assertTrue(custom_list.has_element(1))

        self.assertRaises(InvalidDataType, custom_list.add_to_front, "123")
        self.assertRaises(InvalidDataType, custom_list.add_to_back, "123")

    def test_add_remove(self):
        custom_list = SingleLinkList(int)
        self.list_operations(custom_list)
        custom_list2 = SingleLinkList(int, has_tail=False)
        self.list_operations(custom_list2)

if __name__ == '__main__':
    unittest.main()
