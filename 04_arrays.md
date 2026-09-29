# Arrays & Hashing

## Q1. Subarray Sum Equals K

Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals `k`.

**Example**
```
Input: nums = [1,2,3], k = 3
Output: 2
Explanation: [1,2] and [3]
```

**Constraints**
- `1 ≤ nums.length ≤ 2 * 10^4`
- `-1000 ≤ nums[i] ≤ 1000`
- `-10^7 ≤ k ≤ 10^7`

**Hint:** Prefix sums + hashmap of frequencies. Watch for negative numbers (sliding window alone won't work).

---

## Q2. Product of Array Except Self

Given an integer array `nums`, return an array `answer` such that `answer[i]` is the product of all elements of `nums` except `nums[i]`.

You must write an algorithm that runs in `O(n)` time and **without** using division.

**Example**
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

**Follow-up:** Solve with `O(1)` extra space (output array does not count as extra space).

---

## Q3. Longest Consecutive Sequence

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

Your algorithm must run in `O(n)` time.

**Example**
```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive sequence is [1,2,3,4].
```

**Hint:** Put numbers in a set; only start counting from numbers that have no predecessor (`x - 1` not in set).
