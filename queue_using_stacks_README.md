# Queue Using Stacks

## Problem Description
Implement a first in first out (FIFO) queue using only two stacks. The implementation should support all standard queue operations.

## Operations
- `push(x)`: Push element x to the back of queue
- `pop()`: Remove and return the element from front of queue
- `peek()`: Return the element at front of queue
- `empty()`: Return whether the queue is empty

## Solution Approach
The solution uses two stacks to implement a queue:
1. `stack1`: Used for pushing elements
2. `stack2`: Used for popping elements

### How it works:
- For push: Simply push to stack1
- For pop/peek: 
  - If stack2 is empty, transfer all elements from stack1 to stack2
  - Then pop/peek from stack2
- For empty: Check if both stacks are empty

## Time Complexity
- Push: O(1)
- Pop: Amortized O(1), Worst case O(n)
- Peek: Amortized O(1), Worst case O(n)
- Empty: O(1)

## Space Complexity
O(n) where n is the number of elements in the queue
