from ..lists.SingleLinkList import SingleLinkList
from ..exceptions.custom import (
                    StackUnderFlowException,
                    LinkedListEmpty
                    )

class ListStack:

    def __init__(self, elem_type):
        self.stack = SingleLinkList(elem_type=elem_type, has_tail=False)
        self.top = self.stack.head
        self.elem_type = elem_type

    def stack_empty(self):
        return self.stack.list_empty()
    
    def top_elem(self):
        if self.stack_empty():
            raise StackUnderFlowException
        return self.top.next.data
    
    def pop(self):
        try:
            return self.stack.pop_first_element()
        except LinkedListEmpty:
            raise StackUnderFlowException

    def push(self, elem_type):
        self.stack.add_to_front(elem_type)