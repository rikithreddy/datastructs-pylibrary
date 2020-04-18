from ..common import Node

from ..exceptions.custom import (
                        InvalidArraySize,
                        InvalidDataType,
                        InvalidArrayIndex,
                        InvalidArrayInitializerSize
                        )

class SingleDimensionArray:

    def _check_index(self, index):
        if index < 0 or index >= self.size:
            raise InvalidArrayIndex(
                            "Expected range of index 0 to {}, Provided {}".
                            format(self.size, index)
                            )

    def _check_value(self, elem):
        if not isinstance(elem, self.elem_type):
            raise InvalidDataType(
                            "Expected data object of {}, Recieved {}".format(
                                self.elem_type,
                                type(elem)
                                )
                            )

    def __init__(self, elem_type, size, init=[]):
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
        self._check_index(index)
        return self.array[index].data

    def update(self, index, value):
        self._check_index(index)
        self._check_value(value)
        self.array[index].data = value
