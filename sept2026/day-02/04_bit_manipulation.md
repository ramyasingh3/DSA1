# Counting Bits

## Problem
Number of 1-bits for 0..n.

## Example
```
Input: [27, 21, 15, -9, 7, 33, 29]
Output: (compute according to problem statement)
```

## Constraints
- Reasonable input sizes for interview settings (`n` up to ~10^5 unless noted)
- Aim for better than naive O(n^2) when possible

## Hint
DP: ans[i] = ans[i>>1] + (i&1).

## Topic
Bit Manipulation
