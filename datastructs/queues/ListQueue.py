from ..lists.SingleLinkList import SingleLinkList
from ..exceptions.custom import (
                            QueueEmpty,
                            LinkedListEmpty
                            )

class ListQueue:

    def __init__(self, elem_type):
        self.queue = SingleLinkList(elem_type=elem_type, has_tail=True)
        self.top = self.queue.head
        self.elem_type = elem_type

    def queue_empty(self):
        return self.queue.list_empty()
    
    def next_key(self):
        if self.queue_empty():
            raise QueueEmpty
        return self.top.next.data
    
    def enqueue(self, key):
        self.queue.add_to_back(key)
    
    def dequeue(self):
        try:
            return self.queue.pop_first_element()
        except LinkedListEmpty:
            raise QueueEmpty