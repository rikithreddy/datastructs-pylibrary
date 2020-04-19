from ..common import TreeNode
from ..exceptions.custom import InvalidDataType


class BinaryTree:

    def _check_value(self, elem):
        if not isinstance(elem, self.elem_type):
            raise InvalidDataType(
                            "Expected data object of {}, Recieved {}".format(
                                self.elem_type,
                                type(elem)
                                )
                            )

    def __init__(self, elem_type, data=None):
        self.elem_type = elem_type
        self.root = TreeNode()

    def addLeft(self, data):
        self._check_value(data)
        if self.tree_empty():
            self.add_data(self.root, data)
        else:
            


