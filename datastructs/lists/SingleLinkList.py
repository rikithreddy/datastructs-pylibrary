from ..common import Node
from sys import stdout
from copy import copy

class SingleLinkList:

    def _check_value(self, elem):
        if not isinstance(elem, self.elem_type):
            raise ValueError

    def __init__(self, elem_type, has_tail=True):
        self.head = Node()
        self.has_tail = has_tail
        self.len = 0
        self.elem_type = elem_type

        if has_tail:
            self.tail = self.head

    def list_empty(self):
        return True if self.len == 0 else False

    def get_last_node(self):
        if self.has_tail:
            return self.tail

        temp = self.head
        while temp.next != None:
            temp = temp.next
        return temp

    def add_to_front(self, data):
        self._check_value(data)
        new_node = Node(data=data, next=self.head.next)
        self.head.next = new_node

        if self.list_empty() and self.has_tail:
            self.tail = new_node
        self.len += 1

    def get_first_element(self):
        if self.head.next is not None:
            return self.head.next.data
        else:
            # TODO: Add Error
            print("List is empty")
            raise IndexError

    def pop_first_element(self):
        if self.head and not self.head.next:
            # TODO: Add error
            print("Error List is empty")
            raise IndexError
        if self.has_tail and self.tail == self.head.next:
            self.tail = self.head
        node = self.head.next
        self.head.next = self.head.next.next
        data = node.data
        del node
        self.len -= 1
        return data

    def print_list(self):
        temp = self.head.next
        while temp:
            stdout.write('-->{}'.format(temp.data))
            temp = temp.next
        print()

    def add_to_back(self, data):
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
        if not self.list_empty():
            return self.get_last_node().data
        else:
            # TODO: Add Error
            print("List is empty")
            raise IndexError

    def find_element(self, data):
        '''
        Check if the list has a node with the given data
        Returns an enumerable object for each node found.
        '''
        temp = self.head.next
        index = 0
        while temp!=None:
            if temp.data == data:
                yield temp, index

            temp = temp.next
            index += 1
    
    def has_element(self, data):
        '''
        Check if the list has a particular data object
        '''
        try:
            _ = next(self.find_element(data))
            return True
        except StopIteration:
            return False

        # TODO: Add in Nth position
        # TODO: Add Pop from back