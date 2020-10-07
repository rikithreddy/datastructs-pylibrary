from ..common import Node

from ..exceptions.custom import (
    InvalidArraySize,
    InvalidDataType,
    InvalidArrayIndex,
    InvalidArrayInitializerSize
)


class SingleDimensionArray:
    """
    Class to build one-dimensional arrays
    """

    def _check_index(self, index):
        """
        Function to check for exceptions regarding out of bounds errors

        :param index: number to check array at
        :raise: InvalidArrayIndex: if index passed in is out of range of array's
                size
        :return: none
        """
        if index < 0 or index >= self.size:
            raise InvalidArrayIndex(
                "Expected range of index 0 to {}, Provided {}".
                    format(self.size, index)
            )

    def _check_value(self, elem):
        """
        Function to check for exceptions regarding invalid data types
        :param elem: element to check the data type on
        :raise: InvalidDataType: if element passed in is of the wrong data type
        :return: none
        """
        if not isinstance(elem, self.elem_type):
            raise InvalidDataType(
                "Expected data object of {}, Recieved {}".format(
                    self.elem_type,
                    type(elem)
                )
            )

    def __init__(self, elem_type, size, init=[]):
        """
        Initializes an array if it has not been already.
        :param elem_type: Data type expected
        :param size: size of array
        :param init: array to start with
        :raise: InvalidArrayInitializerSize if the length of init parameter
                does not match size
        :return none
        """
        self.size = size
        self.elem_type = elem_type
        self.array = [Node(data=elem_type()) for _ in range(size)]

        if init:
            if len(init) == size:
                for id, elem in enumerate(init):
                    self._check_value(elem)
                    self.array[id].data = elem
            else:
                raise InvalidArrayInitializerSize

    def get(self, index):
        """
        Gets element at index passed in
        :param index: index to get element from
        :return: element at desired index
        """
        self._check_index(index)
        return self.array[index].data

    def update(self, index, value):
        """
        Checks index and value passed in for exception errors, then puts value
        passed into desired index
        :param index: index to check and place value
        :param value: value to place into desired index
        :return: none
        """
        self._check_index(index)
        self._check_value(value)
        self.array[index].data = value
