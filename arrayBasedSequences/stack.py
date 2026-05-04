# stack.py
# This file contains the Stack class.
# The Stack class uses a Python list internally, but only exposes stack operations.

class Stack:
    def __init__(self):
        # Creates an empty list to store the stack items
        self._items = []

    def push(self, item):
        # Adds an item to the top of the stack
        self._items.append(item)

    def pop(self):
        # Removes and returns the top item from the stack
        if self.is_empty():
            raise Exception("Cannot pop from an empty stack.")
        return self._items.pop()

    def peek(self):
        # Returns the top item without removing it
        if self.is_empty():
            raise Exception("Cannot peek from an empty stack.")
        return self._items[-1]

    def is_empty(self):
        # Returns True if the stack has no items
        return len(self._items) == 0

    def size(self):
        # Returns the number of items in the stack
        return len(self._items)

    # Test code
if __name__ == "__main__":
    stack = Stack()

    print("Is empty?", stack.is_empty())

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top item:", stack.peek())
    print("Size:", stack.size())

    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())

    print("Is empty?", stack.is_empty())