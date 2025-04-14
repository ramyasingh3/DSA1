"""
Problem: Implement Queue using Stacks

Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue:
- push(x): Push element x to the back of queue
- pop(): Removes the element from the front of queue and returns it
- peek(): Returns the element at the front of queue
- empty(): Returns whether the queue is empty

Example:
MyQueue queue = new MyQueue();
queue.push(1);      // queue is: [1]
queue.push(2);      // queue is: [1, 2]
queue.peek();       // returns 1
queue.pop();        // returns 1, queue is [2]
queue.empty();      // returns false
"""

class MyQueue:
    def __init__(self):
        # Stack for pushing elements
        self.stack1 = []
        # Stack for popping elements
        self.stack2 = []

    def push(self, x: int) -> None:
        # Simply push to stack1
        self.stack1.append(x)

    def pop(self) -> int:
        # If stack2 is empty, transfer all elements from stack1
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Pop from stack2
        if self.stack2:
            return self.stack2.pop()
        return None

    def peek(self) -> int:
        # If stack2 is empty, transfer all elements from stack1
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Return top element from stack2
        if self.stack2:
            return self.stack2[-1]
        return None

    def empty(self) -> bool:
        # Queue is empty if both stacks are empty
        return len(self.stack1) == 0 and len(self.stack2) == 0


def test_queue():
    # Test case 1: Basic operations
    print("Test Case 1: Basic Operations")
    queue = MyQueue()
    print("Push 1, 2, 3")
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(f"Peek: {queue.peek()}")  # Should be 1
    print(f"Pop: {queue.pop()}")    # Should be 1
    print(f"Empty: {queue.empty()}") # Should be False
    print("-" * 30)

    # Test case 2: Empty queue operations
    print("Test Case 2: Empty Queue")
    queue = MyQueue()
    print(f"Empty queue - Empty?: {queue.empty()}")  # Should be True
    print(f"Empty queue - Peek: {queue.peek()}")     # Should be None
    print(f"Empty queue - Pop: {queue.pop()}")       # Should be None
    print("-" * 30)

    # Test case 3: Multiple push/pop operations
    print("Test Case 3: Multiple Operations")
    queue = MyQueue()
    print("Push 1, Pop, Push 2, Push 3, Pop, Peek")
    queue.push(1)
    print(f"Pop after first push: {queue.pop()}")  # Should be 1
    queue.push(2)
    queue.push(3)
    print(f"Pop after more pushes: {queue.pop()}")  # Should be 2
    print(f"Peek at remaining: {queue.peek()}")     # Should be 3
    print("-" * 30)

if __name__ == "__main__":
    test_queue()
