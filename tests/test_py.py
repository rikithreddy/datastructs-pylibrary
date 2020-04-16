from datastructs.lists.SingleLinkList import SingleLinkList
import unittest

class TestSingleLinkList(unittest.TestCase):

    def list_operations(self, custom_list):
        self.assertIsNone(custom_list.pop_first_element())
        self.assertIsNone(custom_list.get_first_element())
        self.assertIsNone(custom_list.get_last_element())
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

    def test_add_remove(self):
        custom_list = SingleLinkList()
        self.list_operations(custom_list)
        custom_list2 = SingleLinkList(has_tail=False)
        self.list_operations(custom_list2)

if __name__ == '__main__':
    unittest.main()
