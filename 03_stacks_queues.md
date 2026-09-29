# Stacks & Queues

## Q1. Next Greater Element II (Circular Array)

Given a circular integer array `nums`, for each index `i` find the next greater element — the first larger number when traversing clockwise. If none exists, use `-1`.

**Example**
```
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation:
- For 1 at index 0 → next greater is 2
- For 2 at index 1 → none
- For 1 at index 2 → wraps around to 2
```

**Constraints**
- `1 ≤ nums.length ≤ 10^4`
- `-10^9 ≤ nums[i] ≤ 10^9`

**Hint:** Monotonic decreasing stack; simulate circularity by iterating `2n` times (or use modulo).

---

## Q2. Sliding Window Maximum

You are given an array of integers `nums` and an integer `k`. There is a sliding window of size `k` moving from left to right. Return an array of the maximum value in each window.

**Example**
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
```

**Requirement:** Solve in `O(n)` time using a deque (monotonic queue).

---

## Q3. Design a Min Stack

Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in constant time.

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

**Constraints**
- Methods must each run in `O(1)` average time
- At most `3 * 10^4` calls

**Hint:** Keep a parallel stack of running minima, or store pairs `(value, currentMin)`.
