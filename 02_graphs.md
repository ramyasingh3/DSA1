# Graphs

## Q1. Course Schedule (Detect Cycle in Directed Graph)

There are `numCourses` courses labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` means you must take course `b_i` before course `a_i`.

Return `true` if you can finish all courses, otherwise `false`.

**Example**
```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: Cycle — cannot finish both.
```

**Hint:** Model as a directed graph; use Kahn's algorithm (BFS topological sort) or DFS coloring (white/gray/black).

---

## Q2. Number of Islands

Given an `m x n` 2D binary grid representing a map of `'1'` (land) and `'0'` (water), return the number of islands.

An island is surrounded by water and formed by connecting adjacent lands horizontally or vertically.

**Example**
```
Input:
[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

**Follow-up:** Solve with Union-Find as well as DFS/BFS flood fill.

---

## Q3. Cheapest Flights Within K Stops

There are `n` cities connected by some flights. Each flight is `[from, to, price]`.

Find the cheapest price from `src` to `dst` with at most `k` stops. If no such route exists, return `-1`.

**Example**
```
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
       src = 0, dst = 3, k = 1
Output: 700
Explanation: 0 → 1 → 3 (cost 700). Path 0 → 1 → 2 → 3 uses 2 stops.
```

**Hint:** Bellman-Ford relaxed for `k + 1` iterations, or Dijkstra with (cost, node, stops) state.
