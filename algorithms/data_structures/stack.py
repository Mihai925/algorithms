"""
    Stack data structure:
    ----------------------
    push: push an element to the stack
    pop: pop the last element of the stack
    peek: see the last element from the stack
    is_empty: check if the stack is is empty
    size: return the size of the stack

    Time Complexity: O(1)
"""

class stack:
    
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.__verify_for_get_element()
        return self.stack.pop()

    def peek(self):
        self.__verify_for_get_element()
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return (self.size() == 0)

    def __verify_for_get_element(self):
        if self.is_empty():
            raise IndexError('stack is empty, cannot perform operation')
