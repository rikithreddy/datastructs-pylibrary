from datastructs.lists.SingleLinkList import SingleLinkList
import unittest

class TestList(unittest.TestCase):

    def test_add(self):
        custom_list = SingleLinkList()

        self.assertIsNone(custom_list.pop_first_element())
        custom_list.add_to_front(0)
        custom_list.add_to_back(1)

        self.assertEqual(custom_list.get_last_element(), 1)
        self.assertEqual(custom_list.get_first_element(), 0)

        custom_list.add_to_back(2)
        custom_list.add_to_front(3)

        self.assertEqual(custom_list.pop_first_element(), 3)
        self.assertEqual(custom_list.pop_first_element(), 0)


if __name__ == '__main__':
    unittest.main()
