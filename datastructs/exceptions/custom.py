class StackOverFlowException(Exception):
    def __init__(self, message):
        super().__init__(message)

class StackUnderFlowException(Exception):
    def __init__(self):
        super().__init__("The stack is empty")

class StackEmpty(Exception):
    pass

class QueueEmpty(Exception):
    pass

class LinkedListEmpty(Exception):
    pass

class InvalidArraySize(Exception):
    pass

class InvalidArrayIndex(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidArrayInitializerSize(Exception):
    pass


class InvalidDataType(Exception):
    def __init__(self, msg):
        super().__init__(msg)