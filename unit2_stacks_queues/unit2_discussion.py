"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Adding to the end keeps the most recent item on top for LIFO.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return "Stack is empty."
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek shows the top item without removing it from the stack.
        if self.is_empty():
            return "Stack is empty."
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Adding to the back keeps the first item added at the front for FIFO.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return "Queue is empty."
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front shows the first item without removing it from the queue.
        if self.is_empty():
            return "Queue is empty."
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    print("\n=== STACK DEMO ===")

    stack = Stack()

    # Add four values to demonstrate LIFO behavior.
    stack.push("Open file")
    stack.push("Edit text")
    stack.push("Save file")
    stack.push("Close file")

    print("Top item:", stack.peek())
    print("Removing items in LIFO order:")
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    # Test pop and peek on an empty stack.
    print("Pop from empty stack:", stack.pop())
    print("Peek at empty stack:", stack.peek())

    # Test a stack containing only one item.
    single_stack = Stack()
    single_stack.push("One item")
    print("Single item removed:", single_stack.pop())
    print("Is single-item stack empty?", single_stack.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    queue = Queue()

    # Add four values to demonstrate FIFO behavior.
    queue.enqueue("Customer 1")
    queue.enqueue("Customer 2")
    queue.enqueue("Customer 3")
    queue.enqueue("Customer 4")

    print("Front item:", queue.front())
    print("Removing items in FIFO order:")
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    # Test dequeue and front on an empty queue.
    print("Dequeue from empty queue:", queue.dequeue())
    print("Front of empty queue:", queue.front())

    # Test a queue containing only one item.
    single_queue = Queue()
    single_queue.enqueue("One customer")
    print("Single item removed:", single_queue.dequeue())
    print("Is single-item queue empty?", single_queue.is_empty())

if __name__ == "__main__":
    main()
