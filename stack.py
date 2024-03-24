class Stack:
    def __init__(self, limit=None):
        """Initialize the Stack."""
        self.stack = []  # Initialize an empty list to represent the stack
        self.limit = limit  # Optional limit for the size of the stack

    def push(self, item):
        """Push item onto the stack."""
        if self.limit is None or len(self.stack) < self.limit:
            self.stack.append(item)  # Add item to the stack if not exceeding the limit
        else:
            raise OverflowError("Stack is full")  # Raise an error if stack is full

    def pop(self):
        """Remove and return the last item from the stack."""
        if self.is_empty():
            raise IndexError("Stack is empty")  # Raise an error if stack is empty
        return self.stack.pop()  # Remove and return the last item from the stack

    def peek(self):
        """Return the last item from the stack."""
        if self.is_empty():
            raise IndexError("Stack is empty")  # Raise an error if stack is empty
        return self.stack[-1]  # Return the last item from the stack

    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""
        return len(self.stack) == 0  # Check if the stack is empty

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.stack)  # Return the number of elements in the stack

    def search(self, value):
        """
        Return the distance between the top of the stack
        and the target element if it's present; -1 otherwise.
        If the target element is at the top of the stack,
        return 0.
        """
        if self.is_empty():
            return -1  # Return -1 if the stack is empty
        try:
            index = self.stack.index(value)  # Find the index of the value in the stack
            return len(self.stack) - index - 1  # Calculate the distance from the top of the stack
        except ValueError:
            return -1  # Return -1 if the value is not found in the stack

    def is_full(self):
        """Return True if the stack is full, False otherwise."""
        if self.limit is not None:
            return len(self.stack) == self.limit  # Check if the stack is full based on the limit
        else:
            return False  # If no limit is set, the stack is not full
