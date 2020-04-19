class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None