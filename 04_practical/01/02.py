# Implement a stack using a list. Include push, pop, peek, and is_empty methods.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # Add item to the top of the stack

    def pop(self):
        return self.items.pop() if not self.is_empty() else None  # Remove item from the top

    def peek(self):
        return self.items[-1] if not self.is_empty() else None  # View the top item without removing

    def is_empty(self):
        return len(self.items) == 0  # Check if the stack is empty
