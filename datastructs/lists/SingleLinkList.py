from ..common import Node
from sys import stdout
from copy import copy

from ..exceptions.custom import (
    InvalidDataType,
    LinkedListEmpty
)


class SingleLinkList:
    """
    Class to build Single Linked List data structures
    """

    def _check_value(self, elem):
        """
        Function to check data type of element passed in
        :param elem: element to check data type of
        :raise: InvalidDataType if element passed does not have set element type
        :return: none
        """
        if not isinstance(elem, self.elem_type):
            raise InvalidDataType(
                "Expected data object of {}, Received {}".format(
                    self.elem_type,
                    type(elem)
                )
            )

    def __init__(self, elem_type, has_tail=True):
        """
        Initializer for Single Linked List data structure
        :param elem_type: Data type expected this instance of SingleLinkList
        :param has_tail: boolean parameter to indicate if SingleLinkList has a
                         a tail
        :return: none
        """
        self.head = Node()
        self.has_tail = has_tail
        self.len = 0
        self.elem_type = elem_type

        if has_tail:
            self.tail = self.head

    def list_empty(self):
        """
        Function to check if SingleLinkList is empty
        :return: True if SingleLinkList is empty, False otherwise
        """
        return True if self.len == 0 else False

    def get_last_node(self):
        """
        Function to get the last node of the SingleLinkList
        :return: Last node in SingleLinkList
        """
        if self.has_tail:
            return self.tail

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        return temp

    def add_to_front(self, data):
        """
        Function to add a node to the front of the SingleLinkList
        :param data: Data to store in new node
        :return: none
        """
        self._check_value(data)
        new_node = Node(data=data, next=self.head.next)
        self.head.next = new_node

        if self.list_empty() and self.has_tail:
            self.tail = new_node
        self.len += 1

    def get_first_element(self):
        """
        Function to get head of SingleLinkList
        :raise: LinkedListEmpty if head is None
        :return: head of SingleLinkList
        """
        if self.head.next is not None:
            return self.head.next.data
        else:
            raise LinkedListEmpty

    def pop_first_element(self):
        """
        Function to get first node in SingleLinkList, then remove it
        :raise: LinkedListEmpty if head is the node popped
        :return: data in the head node
        """
        if self.head and not self.head.next:
            raise LinkedListEmpty

        if self.has_tail and self.tail == self.head.next:
            self.tail = self.head
        node = self.head.next
        self.head.next = self.head.next.next
        data = node.data
        del node
        self.len -= 1
        return data

    def print_list(self):
        """
        Function to print off elements in SingleLinkList
        :return: none
        """
        temp = self.head.next
        while temp:
            stdout.write('-->{}'.format(temp.data))
            temp = temp.next
        print()

    def add_to_back(self, data):
        """
        Function to add a node to the back of the list
        :param data: data to store in node to be placed in the back
        :return: none
        """
        self._check_value(data)
        node = Node(data=data)

        self.len += 1

        if self.list_empty():
            self.head.next = node
            if self.has_tail:
                self.tail = node
            return

        if self.has_tail:
            self.tail.next = node
            self.tail = node
        else:
            temp = self.get_last_node()
            temp.next = node

    def get_last_element(self):
        """
        Function to retrieve tail of SingleLinkList
        :return: tail of SingleLinkList
        """
        if not self.list_empty():
            return self.get_last_node().data
        else:
            raise LinkedListEmpty

    def find_element(self, data):
        """
        Check if the list has a node with the given data
        Returns an enumerable object for each node found.
        """
        temp = self.head.next
        index = 0
        while temp is not None:
            if temp.data == data:
                yield temp, index

            temp = temp.next
            index += 1

    def has_element(self, data):
        """
        Check if the list has a particular data object
        """
        try:
            _ = next(self.find_element(data))
            return True
        except StopIteration:
            return False

        # TODO: Add in Nth position
        # TODO: Add Pop from back
