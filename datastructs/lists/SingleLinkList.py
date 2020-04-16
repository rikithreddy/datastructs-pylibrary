from ..common import Node
from sys import stdout
from copy import copy

class SingleLinkList:
    def __init__(self, has_tail=True):
        self.head = Node()
        self.has_tail = has_tail
        self.len = 0

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

    def pop_first_element(self):
        if self.head and not self.head.next:
            # TODO: Add error
            print("Error List is empty")
            return
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
            __ = next(self.find_element(data))
            return True
        except StopIteration:
            return False