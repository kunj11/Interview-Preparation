
# DSA Patterns Cheat Sheet (Backend Engineer Edition)

A quick revision guide for **common Data Structure & Algorithm patterns** frequently asked in **non‑FAANG backend interviews**.

Goal: Recognize patterns quickly and implement them confidently.

---

## Table of Contents

1. Arrays
2. HashMap / HashSet
3. Two Pointers
4. Sliding Window
5. Stack
6. Linked List (Fast / Slow Pointer)
7. Binary Search
8. Tree Traversal (DFS / BFS)
9. Recursion
10. Backtracking
11. Dynamic Programming (Basic)
12. Heap / Priority Queue

---

# 1. Arrays

## When To Use

- Iterating through data
- Prefix/suffix computations
- Subarray problems

## Common Problems

| Problem |
|---|
| Two Sum |
| Product of Array Except Self |
| Maximum Subarray |
| Longest Consecutive Sequence |

## Python Template

```python
for i in range(len(nums)):
    # process element
    pass
```

## Key Trick

Prefix / suffix arrays

```python
prefix[i] = prefix[i-1] + nums[i]
```

---

# 2. HashMap / HashSet

## When To Use

- Fast lookups
- Frequency counting
- Checking duplicates

## Common Problems

| Problem |
|---|
| Two Sum |
| Valid Anagram |
| Contains Duplicate |
| Group Anagrams |

## Python Template

```python
seen = {}

for num in nums:
    if num in seen:
        return True
    seen[num] = True
```

Lookup complexity: **O(1)** average

---

# 3. Two Pointers

## When To Use

- Sorted arrays
- Pair problems
- Palindrome checks

## Common Problems

| Problem |
|---|
| Valid Palindrome |
| Two Sum II |
| Container With Most Water |
| 3Sum |

## Visual Idea

```
L →        ← R
[1,2,3,4,5,6]
```

## Python Template

```python
l, r = 0, len(nums) - 1

while l < r:
    if condition:
        l += 1
    else:
        r -= 1
```

---

# 4. Sliding Window

## When To Use

- Subarray / substring problems
- Longest or shortest window

## Common Problems

| Problem |
|---|
| Longest Substring Without Repeating |
| Minimum Window Substring |
| Maximum Sum Subarray |

## Visual Idea

```
[ start → window → end ]
```

## Python Template

```python
left = 0

for right in range(len(nums)):

    # expand window

    while invalid_condition:
        left += 1
```

---

# 5. Stack

## When To Use

- Parentheses validation
- Next greater element
- Reversing order

## Common Problems

| Problem |
|---|
| Valid Parentheses |
| Daily Temperatures |
| Next Greater Element |
| Min Stack |

## Python Template

```python
stack = []

for x in nums:
    while stack and stack[-1] < x:
        stack.pop()
    stack.append(x)
```

---

# 6. Linked List (Fast / Slow Pointer)

## When To Use

- Cycle detection
- Finding middle node
- Linked list traversal

## Visual Idea

```
slow → 1 → 2 → 3 → 4 → 5
fast → 1 → 3 → 5
```

## Common Problems

| Problem |
|---|
| Linked List Cycle |
| Middle of Linked List |
| Remove Nth Node |
| Reverse Linked List |

## Python Template

```python
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

---

# 7. Binary Search

## When To Use

- Sorted arrays
- Search problems
- Min / max optimization

## Common Problems

| Problem |
|---|
| Binary Search |
| Search Insert Position |
| Find Peak Element |
| Search Rotated Array |

## Python Template

```python
l, r = 0, len(nums) - 1

while l <= r:
    mid = (l + r) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        l = mid + 1
    else:
        r = mid - 1
```

---

# 8. Tree Traversal

## DFS

Traversal types:

- Preorder
- Inorder
- Postorder

```python
def dfs(node):
    if not node:
        return

    dfs(node.left)
    dfs(node.right)
```

## BFS

```python
from collections import deque

queue = deque([root])

while queue:
    node = queue.popleft()
```

---

# 9. Recursion

## Template

```python
def solve(problem):

    if base_case:
        return

    solve(sub_problem)
```

---

# 10. Backtracking

## When To Use

- Permutations
- Combinations
- Subsets

## Template

```python
def backtrack(path):

    if solution_found:
        result.append(path.copy())
        return

    for choice in choices:
        path.append(choice)
        backtrack(path)
        path.pop()
```

---

# 11. Dynamic Programming

## Common Problems

| Problem |
|---|
| Climbing Stairs |
| House Robber |
| Maximum Subarray |

## Template

```python
dp = [0] * n

for i in range(2, n):
    dp[i] = dp[i-1] + dp[i-2]
```

---

# 12. Heap / Priority Queue

## When To Use

- Top K elements
- Scheduling problems

## Template

```python
import heapq

heap = []

heapq.heappush(heap, value)
heapq.heappop(heap)
```

---

# Pattern Recognition Quick Guide

| If Problem Mentions | Pattern |
|---|---|
| pair in array | Two Pointers / HashMap |
| longest substring | Sliding Window |
| next greater element | Stack |
| sorted array search | Binary Search |
| tree traversal | DFS / BFS |
| combinations | Backtracking |
| maximize/minimize result | Dynamic Programming |

---

# Final Advice

Before interviews:

1. Review this cheat sheet
2. Solve 2–3 problems per pattern
3. Practice explaining solutions clearly


Goal:

Backend Engineer  +  Solid DSA Fundamentals  =  Interview Ready
