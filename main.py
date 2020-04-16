from lists.SingleLinkList import SingleLinkList

if __name__ == "__main__":
   list_node = SingleLinkList(True)
   list_node.add_to_front(1)
   list_node.add_to_front(2)
   list_node.add_to_front(3)
   print(list_node.pop_first_element())
   print(list_node.tail.data)
   print(list_node.pop_first_element())
   print(list_node.tail.data)
   print(list_node.pop_first_element())
   print(list_node.tail.data)