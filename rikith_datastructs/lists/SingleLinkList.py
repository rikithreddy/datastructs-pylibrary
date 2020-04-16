from ..common import Node
from sys import stdout
from copy import copy

class SingleLinkList:

    def __init__(self, has_tail=True):
        self.head = Node()
        self.has_tail = has_tail

        if has_tail:
            self.tail = self.head

    def list_empty(self):
        return False if self.head.next else True

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

        if self.has_tail and self.tail == self.head:
            self.tail = new_node

    def get_first_element(self):
        if self.head.next is not None:
            return self.head.next.data
        else:
            # TODO: Add Error log
            print("List is empty")

    def pop_first_element(self):
        if self.head and not self.head.next:
            # TODO: Add error log
            print("Error List is empty")
            return
        if self.has_tail and self.tail == self.head.next:
            self.tail = self.head
        node = self.head.next
        self.head.next = self.head.next.next
        data = node.data
        del node
        return data

    def print_list(self):
        temp = self.head.next
        while temp:
            stdout.write('-->{}'.format(temp.data))
            temp = temp.next
        print()

    def add_to_back(self, data):
        node = Node(data=data)

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
            # TODO: Add log
            print("List is empty")